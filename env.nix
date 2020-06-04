with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "python-dev-env";

  buildInputs = [
    pkgs.figlet
    pkgs.lolcat
    pkgs.python3
    pkgs.python37Packages.pip
    pkgs.python37Packages.black
    pkgs.python37Packages.flake8
    pkgs.python37Packages.pytest
  ];

  shellHook = ''
    figlet "Bem vindo!" | lolcat --freq 0.5
  '';
}
