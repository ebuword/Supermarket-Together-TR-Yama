import tempfile
import unittest
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "installer"))

import setup_installer as installer


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.game = Path(self.temp.name) / "Supermarket Together"
        self.game.mkdir()
        (self.game / installer.GAME_EXE).write_bytes(b"test executable")
        self.payload = REPO / "installer" / "mod_data"

    def tearDown(self):
        self.temp.cleanup()

    def test_install_and_verify_compatibility_settings(self):
        result = installer.install_patch(
            self.game,
            self.payload,
            check_process=False,
        )
        config = (self.game / "BepInEx/config/AutoTranslatorConfig.ini").read_text(encoding="utf-8")
        self.assertIn(r"Directory=Translation\{Lang}\Text", config)
        self.assertNotIn(r"Directory=BepInEx\Translation", config)
        self.assertIn("EnableUIElements=True", config)
        self.assertIn("EnableTextMeshPro=True", config)
        self.assertIn("Tag=5.6.2", config)
        self.assertGreaterEqual(result["translation_pairs"], 1600)
        self.assertFalse((self.game / "BepInEx/BepInEx").exists())
        self.assertEqual(
            (self.game / "BepInEx/Translation/tr/.tr_version").read_text(encoding="utf-8").strip(),
            installer.VERSION,
        )
        self.assertTrue((self.game / "BepInEx/Translation/tr/installation.json").is_file())

    def test_existing_files_are_backed_up(self):
        old = self.game / "winhttp.dll"
        old.write_bytes(b"old winhttp")
        result = installer.install_patch(
            self.game,
            self.payload,
            check_process=False,
        )
        backup = Path(result["backup"])
        self.assertEqual((backup / "winhttp.dll").read_bytes(), b"old winhttp")
        self.assertNotEqual(old.read_bytes(), b"old winhttp")

    def test_invalid_folder_is_rejected(self):
        (self.game / installer.GAME_EXE).unlink()
        with self.assertRaises(ValueError):
            installer.install_patch(self.game, self.payload, check_process=False)

    def test_libraryfolders_parser(self):
        vdf = Path(self.temp.name) / "libraryfolders.vdf"
        vdf.write_text('"path" "F:\\\\SteamLibrary"\n"path" "D:\\\\Games"', encoding="utf-8")
        self.assertEqual(
            installer.parse_libraryfolders(vdf),
            [Path(r"F:\SteamLibrary"), Path(r"D:\Games")],
        )


if __name__ == "__main__":
    unittest.main()
