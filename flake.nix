{
  description = "Basic Flask environment.";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    system = "x86_64-linux";
    pkgs = import nixpkgs {inherit system;};
    python = pkgs.python311;
    lib = nixpkgs.lib;
    # read python pkgs from requirements.txt
    requirements = builtins.filter (x: x != "") (lib.splitString "\n" (builtins.readFile ./requirements.txt));
    flaskEnv = python.withPackages (ps: builtins.map (pkg: builtins.getAttr pkg ps) (builtins.filter (pkg: builtins.hasAttr pkg ps) requirements));

    # Flask start script
    flaskApp = pkgs.writeShellScriptBin "start-flask" ''
      exec ${flaskEnv}/bin/gunicorn --config gunicorn-cfg.py run:app
    '';
  in {
    # Interactive shell
    devShell.${system} = pkgs.mkShell {
      buildInputs = [flaskEnv];
      shellHook = ''
        PS1='\n\[\e[1m\][\[\e[0;33m\]\H\[\e[0;1m\]]\[\e[0m\]:$PWD | \[\e[0;2m\] $(git branch 2>/dev/null | grep '"'"'*'"'"' | colrm 1 2)\n\[\e[0m\]\$ '
        export $(grep -v '^#' .env | sed 's/#.*//' | xargs)
        echo "[INFO]: Dev environment started."
      '';
    };

    # Flask app as shell script
    packages.${system}.default = flaskApp;
  };
}
