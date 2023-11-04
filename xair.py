#Configuração e coanexão inicial
'''
/config/chlink OFF OFF OFF OFF OFF OFF OFF OFF
/config/buslink OFF OFF OFF
/config/linkcfg ON ON ON ON
/config/solo   0.0 LRAFL 0.0 PFL PFL -20 OFF OFF OFF OFF
/config/amixenable OFF OFF
/config/amixlock OFF OFF
/config/mute OFF OFF OFF OFF
'''

#Referenpte a um canal
''' 
/ch/01/config "01 Zé" 3 In01 U01
/ch/01/preamp +0.0 OFF OFF ON 178
/ch/01/gate OFF GATE -80.0 60.0 1  502 983 SELF
/ch/01/gate/filter OFF 3.0 990.9
/ch/01/dyn ON COMP PEAK LOG -39.5 3.0 5 6.50 10 10.0 151 100 SELF OFF
/ch/01/dyn/filter ON 3.0 611.0
/ch/01/insert OFF OFF
/ch/01/eq ON
/ch/01/eq/1 PEQ 351.6 -4.50 1.0
/ch/01/eq/2 PEQ 2k04 +0.50 2.0
/ch/01/eq/3 PEQ 3k31 +2.75 1.8
/ch/01/eq/4 HShv 11k91 +2.50 2.0
/ch/01/mix OFF -12.1 ON -2
/ch/01/mix/01   -oo OFF POSTEQ -100
/ch/01/mix/02  -1.5 OFF POSTEQ
/ch/01/mix/03   -oo OFF POSTEQ -100
/ch/01/mix/04   -oo OFF POSTEQ
/ch/01/mix/05   -oo OFF POSTEQ -100
/ch/01/mix/06   -oo OFF POSTEQ
/ch/01/mix/07   -oo OFF POST
/ch/01/mix/08   -oo OFF POST
/ch/01/mix/09   -oo OFF POST
/ch/01/mix/10   -oo OFF POST
/ch/01/grp %0000 %0001
/ch/01/automix OFF  +0.0
'''

# Inicio do bloco do canal auxiliar
'''
/rtn/aux/config "" 1 U1718
/rtn/aux/preamp +0.0 OFF
/rtn/aux/eq ON
/rtn/aux/eq/1 PEQ 124.7 +0.00 2.0
/rtn/aux/eq/2 PEQ 496.6 +0.00 2.0
/rtn/aux/eq/3 PEQ 1k97 +0.00 2.0
/rtn/aux/eq/4 HShv 10k02 +0.00 2.0
/rtn/aux/mix OFF   -oo ON +0
/rtn/aux/mix/01   -oo OFF POSTEQ +0
/rtn/aux/mix/02   -oo OFF POSTEQ
/rtn/aux/mix/03   -oo OFF POSTEQ +0
/rtn/aux/mix/04   -oo OFF POSTEQ
/rtn/aux/mix/05   -oo OFF POSTEQ +0
/rtn/aux/mix/06   -oo OFF POSTEQ
/rtn/aux/mix/07   -oo OFF POST
/rtn/aux/mix/08   -oo OFF POST
/rtn/aux/mix/09   -oo OFF POST
/rtn/aux/mix/10   -oo OFF POST
/rtn/aux/grp %0000 %0000
'''

# Início da bloco 
''' 
/rtn/1/config "" 2 U0102
/rtn/1/preamp +0.0 OFF
/rtn/1/eq ON
/rtn/1/eq/1 PEQ 124.7 +0.00 2.0
/rtn/1/eq/2 PEQ 496.6 +0.00 2.0
/rtn/1/eq/3 PEQ 1k97 +0.00 2.0
/rtn/1/eq/4 HShv 10k02 +0.00 2.0
/rtn/1/mix ON   0.0 ON +0
/rtn/1/mix/01   -oo OFF POSTEQ +0
/rtn/1/mix/02   -oo OFF POST
/rtn/1/mix/03   -oo OFF POST +0
/rtn/1/mix/04   -oo OFF POST
/rtn/1/mix/05   -oo OFF POST +0
/rtn/1/mix/06   -oo OFF POST
/rtn/1/mix/07   -oo OFF POST
/rtn/1/mix/08   -oo OFF POST
/rtn/1/mix/09   -oo OFF POST
/rtn/1/mix/10   -oo OFF POST
/rtn/1/grp %0000 %0000
'''

# Referente a um barramento 
'''
/bus/1/config "" 3
/bus/1/dyn OFF COMP PEAK LOG 0.0 3.0 1 0.00 10 10.0 151 100 SELF OFF
/bus/1/dyn/filter OFF 3.0 990.9
/bus/1/insert OFF OFF
/bus/1/eq ON PEQ
/bus/1/eq/1 LShv 33.6 +7.50 2.0
/bus/1/eq/2 PEQ 158.9 +0.00 2.0
/bus/1/eq/3 PEQ 496.6 +0.00 2.0
/bus/1/eq/4 PEQ 1k97 +0.00 2.0
/bus/1/eq/5 PEQ 5k02 +0.00 2.0
/bus/1/eq/6 HShv 10k02 +0.00 2.0
/bus/1/geq 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
/bus/1/mix ON  -3.6 OFF +0
/bus/1/grp %0000 %0000
'''

#
'''
/fxsend/1/config "" 4
/fxsend/1/mix ON   0.0
/fxsend/1/grp %0000 %0000
/fxsend/2/config "" 4
/fxsend/2/mix ON   0.0
/fxsend/2/grp %0000 %0000
/fxsend/3/config "" 4
/fxsend/3/mix ON   0.0
/fxsend/3/grp %0000 %0000
/fxsend/4/config "" 4
/fxsend/4/mix ON   0.0
/fxsend/4/grp %0000 %0000
'''


# Bloco LR
'''
/lr/config "" 6
/lr/dyn OFF COMP PEAK LOG 0.0 3.0 1 0.00 10 10.0 151 100 OFF
/lr/dyn/filter OFF 3.0 990.9
/lr/insert OFF OFF
/lr/eq ON GEQ
/lr/eq/1 LShv 79.6 +0.00 2.0
/lr/eq/2 PEQ 224.4 +0.00 2.0
/lr/eq/3 PEQ 496.6 +0.00 2.0
/lr/eq/4 PEQ 2k04 +0.00 2.0
/lr/eq/5 PEQ 5k02 +0.00 2.0
/lr/eq/6 HShv 10k02 +0.00 2.0
/lr/geq 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
/lr/mix ON  -1.4 +0
'''