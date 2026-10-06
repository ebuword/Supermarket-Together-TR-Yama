$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

python -m pip install --disable-pip-version-check -r requirements-build.txt
python -m unittest discover -s tests -v
python -m PyInstaller --noconfirm --clean --onefile --windowed `
  --name "Supermarket_Together_TR_Yama_v12.27.4-fixed.1" `
  --icon "installer/assets/game_icon.ico" `
  --version-file "installer/version_info.txt" `
  --add-data "installer/mod_data;mod_data" `
  "installer/setup_installer.py"

Write-Host "Build tamamlandı: dist/Supermarket_Together_TR_Yama_v12.27.4-fixed.1.exe"
