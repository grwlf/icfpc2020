#{ pkgs ?  import ./lib/nixpkgs {}
{ pkgs ?  import <nixpkgs> {}
, stdenv ? pkgs.stdenv
} :
let

  self = pkgs.python37Packages;
  inherit (pkgs) fetchgit fetchFromGitHub;
  inherit (self) buildPythonPackage fetchPypi;

  pyls = self.python-language-server.override { providers=["pycodestyle" "pyflakes"]; };
  pyls-mypy = self.pyls-mypy.override { python-language-server=pyls; };


  parsec = buildPythonPackage rec {
    name = "parsec";
    src = fetchgit {
      url = "https://github.com/sighingnow/parsec.py";
      rev = "706ee10cd4a426dbbebbe2246a23172aebb5691f";
      sha256 = "sha256:1dlrlvb4b9y1lmbqfsmzg854aap94gdsi63mcy3iqqdfir3zr8ym";
    };
  };

  be = pkgs.mkShell {
    name = "pythonshell";
    buildInputs =
    ( with pkgs;
      with self;
    [
      ipython
      pyls-mypy
      pyls
      # yapf
      # rope
      # pylint
      # pydocstyle
      # autopep8

      numpy
      pandas
      parsec
    ]);

    shellHook = with pkgs; ''
      if test -f ./env.sh ; then
        . ./env.sh
      fi
    '';
  };

in
  be
