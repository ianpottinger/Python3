#! /usr/bin/env python3		#Allow Unix shell to execute as a Python script
# _*_ coding: UTF-8 _*_		#Enable unicode encoding
#GMT+0BST-1,M3.5.0/01:00:00,M10.5.0/02:00:00

__author__ = "Ian Pottinger"
__date__ = "20/12/2012"
__contact__ = "ianpottinger@me.com"
__version__ = "1.3.5.7.9 even avoidance"
__credits__ = "Commonly known as Potts"
__copyright__ = "Copyleft for balance"
__license__ = "Whatever Potts Decides"
__metadata__ = [__author__, __date__, __contact__, __version__,
                __credits__, __copyright__, __license__]


#https://esoteric.codes/blog/the-128-language-quine-relay
#https://github.com/mame/quine-relay
#http://www.nyx.net/~gthompso/quine.htm

_='_=%r;print _(%%)_';print (_%_) 

print((lambda s:s%s)('print((lambda s:s%%s)(%r))'))

#python -c "x='python -c %sx=%s; print x%%(chr(34),repr(x),chr(34))%s'; print x%(chr(34),repr(x),chr(34))"

$ sudo apt-get install afnix algol68g aplus-fsf aspectj asymptote \
  ats2-lang bash bc bf bsdgames bsh clisp clojure cmake coffeescript \
  dafny dc dhall elixir emacs-nox erlang f2c fish flex fp-compiler \
  fsharp g++ gambas3-gb-pcre gambas3-scripter gap gawk gcc gdb gdc \
  generator-scripting-language genius gforth gfortran ghc ghostscript \
  gnat gnu-smalltalk gnucobol4 gnuplot gobjc golang gpt groovy guile-3.0 \
  gzip haxe icont iconx intercal iverilog jasmin-sable jq ksh \
  libpolyml-dev lisaac livescript llvm lua5.3 m4 make maxima minizinc \
  mono-devel mono-mcs mono-vbnc nasm neko nickle node-typescript nodejs \
  ocaml octave openjdk-11-jdk pari-gp parser3-cgi perl php-cli polyml \
  python3 r-base rakudo ratfor rc regina-rexx ruby ruby-mustache rustc \
  scala scilab-cli sed slsh spin squirrel3 surgescript swi-prolog tcl \
  tcsh valac vim wabt xsltproc yabasic yorick zoem zsh

$ sudo apt-get install cmake libpng-dev libgd-dev groff bison curl
$ make -C vendor

$ ulimit -s unlimited
$ ruby QR.rb > QR.rs
$ rustc QR.rs && ./QR > QR.scala
$ scalac QR.scala && scala QR > QR.scm
$ guile QR.scm > QR.sci
$ scilab-cli -nb -f QR.sci > QR.sed
$ sed -E -f QR.sed QR.sed > QR.spl
$ ./vendor/local/bin/spl2c < QR.spl > QR.spl.c && gcc -z muldefs -o QR -I ./vendor/local/include -L ./vendor/local/lib QR.spl.c -lspl -lm &&
  ./QR > QR.sl
$ slsh QR.sl > QR.st
$ gst QR.st > QR.nut
$ squirrel QR.nut > QR.sml
$ polyc -o QR QR.sml && ./QR > QR.sq
$ ruby vendor/subleq.rb QR.sq > QR.ss
$ surgescript QR.ss > QR.tcl
$ tclsh QR.tcl > QR.tcsh
$ tcsh QR.tcsh > QR.t
$ ruby vendor/thue.rb QR.t > QR.ts
$ tsc --outFile QR.ts.js QR.ts && nodejs QR.ts.js > QR.unl
$ ruby vendor/unlambda.rb QR.unl > QR.vala
$ valac QR.vala && ./QR > QR.mid
$ mono vendor/local/bin/Vlt.exe /s QR.mid && mono QR.exe > QR.v
$ iverilog -o QR QR.v && ./QR -vcd-none > QR.vim
$ vim -EsS QR.vim > QR.vb
$ vbnc QR.vb && mono ./QR.exe > QR.wasm
$ $(WASI_RUNTIME) QR.wasm > QR.wat
$ wat2wasm QR.wat -o QR.wat.wasm && $(WASI_RUNTIME) QR.wat.wasm > QR.ws
$ ruby vendor/whitespace.rb QR.ws > QR.xslt
$ xsltproc QR.xslt > QR.yab
$ yabasic QR.yab > QR.yorick
$ yorick -batch QR.yorick > QR.azm
$ zoem -i QR.azm > QR.zsh
$ zsh QR.zsh > QR.+
$ a+ QR.+ > qr.adb
$ gnatmake qr.adb && ./qr > QR.als
$ LANG=C LD_LIBRARY_PATH=/usr/lib/afnix axi QR.als > QR.aheui
$ ruby vendor/aheui.rb QR.aheui > QR.a68
$ a68g QR.a68 > QR.ante
$ ruby vendor/ante.rb QR.ante > QR.aj
$ ajc QR.aj && java QR > QR.asy
$ asy QR.asy > QR.dats
$ patscc -o QR QR.dats && ./QR > QR.awk
$ awk -f QR.awk > QR.bash
$ bash QR.bash > QR.bc
$ BC_LINE_LENGTH=4000000 bc -q QR.bc > QR.bsh
$ bsh QR.bsh > QR.bef
$ cfunge QR.bef > QR.Blc
$ ruby vendor/blc.rb < QR.Blc > QR.bf
$ bf -c500000 QR.bf > QR.c
$ gcc -o QR QR.c && ./QR > QR.cpp
$ g++ -o QR QR.cpp && ./QR > QR.cs
$ mcs QR.cs && mono QR.exe > QR.chef
$ PERL5LIB=vendor/local/lib/perl5 compilechef QR.chef QR.chef.pl &&
  perl QR.chef.pl > QR.clj
$ clojure QR.clj > QR.cmake
$ cmake -P QR.cmake > QR.cob
$ cobc -O2 -x QR.cob && ./QR > QR.coffee
$ coffee --nodejs --stack_size=100000 QR.coffee > QR.lisp
$ clisp QR.lisp > QR.d
$ gdc -o QR QR.d && ./QR > QR.dfy
$ dafny QR.dfy && mono QR.exe > QR.dc
$ dc QR.dc > QR.dhall || true
$ dhall text --file QR.dhall > QR.exs
$ elixir QR.exs > QR.el
$ emacs -Q --script QR.el > QR.erl
$ escript QR.erl > QR.fsx
$ fsharpc QR.fsx -o QR.exe && mono QR.exe > QR.false
$ ruby vendor/false.rb QR.false > QR.fl
$ flex -o QR.fl.c QR.fl && gcc -o QR QR.fl.c && ./QR > QR.fish
$ fish QR.fish > QR.fs
$ gforth QR.fs > QR.f
$ gfortran -o QR QR.f && ./QR > QR.f90
$ gfortran -o QR QR.f90 && ./QR > QR.gbs
$ gbs3 QR.gbs > QR.g
$ gap -q QR.g > QR.gdb
$ gdb -q -x QR.gdb > QR.gel
$ genius QR.gel > QR.gsl
$ gsl -q QR.gsl > QR.plt
$ gnuplot QR.plt > QR.go
$ go run QR.go > QR.gs
$ ruby vendor/golfscript.rb QR.gs > QR.gpt
$ mv QR.c QR.c.bak && gpt -t QR.c QR.gpt && gcc -o QR QR.c && ./QR > QR.grass &&
  mv QR.c.bak QR.c
$ ruby vendor/grass.rb QR.grass > QR.groovy
$ groovy QR.groovy > QR.gz
$ gzip -cd QR.gz > QR.hs
$ ghc QR.hs && ./QR > QR.hx
$ haxe -main QR -neko QR.n && neko QR.n > QR.icn
$ icont -s QR.icn && ./QR > QR.i
$ ick -bfOc QR.i && gcc -static QR.c -I /usr/include/ick-* -o QR -lick &&
  ./QR > QR.j
$ jasmin QR.j && java QR > QR.java
$ javac QR.java && java QR > QR.js
$ nodejs QR.js > QR.jq
$ jq -r -n -f QR.jq > QR.jsfuck
$ nodejs --stack_size=100000 QR.jsfuck > QR.kt
$ kotlinc QR.kt -include-runtime -d QR.jar && kotlin QR.jar > QR.ksh
$ ksh QR.ksh > QR.lazy
$ lazyk QR.lazy > qr.li
$ lisaac qr.li && ./qr > QR.ls
$ lsc QR.ls > QR.ll
$ llvm-as QR.ll && lli QR.bc > QR.lol
$ lci QR.lol > QR.lua
$ lua5.3 QR.lua > QR.m4
$ m4 QR.m4 > QR.mk
$ make -f QR.mk > QR.mac
$ maxima -q --init-mac=QR.mac > QR.mzn
$ minizinc --solver Gecode --soln-sep '' QR.mzn > QR.il
$ ilasm QR.il && mono QR.exe > QR.mustache
$ mustache QR.mustache QR.mustache > QR.asm
$ nasm -felf QR.asm && ld -m elf_i386 -o QR QR.o && ./QR > QR.neko
$ nekoc QR.neko && neko QR.n > QR.5c
$ nickle QR.5c > QR.m
$ gcc -o QR QR.m && ./QR > QR.ml
$ ocaml QR.ml > QR.octave
$ mv QR.m QR.m.bak && octave -qf QR.octave > QR.ook && mv QR.m.bak QR.m
$ ruby vendor/ook-to-bf.rb QR.ook QR.ook.bf && bf -c500000 QR.ook.bf > QR.gp
$ gp -f -q QR.gp > QR.p
$ parser3 QR.p > QR.pas
$ fpc QR.pas && ./QR > QR.pl
$ perl QR.pl > QR.pl6
$ perl6 QR.pl6 > QR.php
$ php QR.php > QR.png
$ npiet QR.png > QR.ps
$ gs -dNODISPLAY -q QR.ps > QR.ppt
$ ppt -d < QR.ppt > QR.prolog
$ swipl -q -t qr -f QR.prolog > QR.pr
$ spin -T QR.pr > QR.py
$ python3 QR.py > QR.R
$ R --slave -f QR.R > QR.ratfor
$ ratfor -o QR.ratfor.f QR.ratfor && gfortran -o QR QR.ratfor.f &&
  ./QR > QR.rc
$ rc QR.rc > QR.rexx
$ rexx ./QR.rexx > QR2.rb



sudo docker build -t qr .
sudo docker run --privileged --rm -e CI=true qr

sudo docker run --privileged --rm -e CI=true -v $(pwd):/usr/local/share/quine-relay -v /usr/local/share/quine-relay/vendor qr


