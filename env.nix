with import <nixpkgs> {};

stdenv.mkDerivation {
  name = "python-dev-env";

  buildInputs = [
    pkgs.figlet
    pkgs.lolcat
    pkgs.python3
    pkgs.python37Packages.pip
  ];

  shellHook = ''
    figlet "Bem vindo!" | lolcat --freq 0.5
  '';
}
