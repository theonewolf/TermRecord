DYNAMIC_OBJS	=	examples/figlet-dynamic.html examples/gcc-dynamic.html \
				    examples/hello-dynamic.html \
					examples/htop-dynamic.html
STATIC_OBJS		=	examples/figlet-static.html examples/gcc-static.html \
				    examples/hello-static.html examples/htop-static.html
DYN_DEP			=	templates/dynamic.jinja2 templates/base.jinja2
STATIC_DEP		=	templates/static.jinja2 templates/base.jinja2

default: dynamic static
dynamic: ${DYNAMIC_OBJS}
static: ${STATIC_OBJS}

examples/%-dynamic.html: ${DYN_DEP} examples/%.time examples/%.script
	src/TermRecord -s examples/${*F}.script -t examples/${*F}.time \
				   -m templates/dynamic.jinja2 \
				   -d 30 80 \
				   -o examples/${*F}-dynamic.html

examples/%-static.html: ${STATIC_DEP} examples/%.time examples/%.script
	src/TermRecord -s examples/${*F}.script -t examples/${*F}.time \
				   -m templates/static.jinja2 \
				   -d 30 80 \
				   -o examples/${*F}-static.html

ttyrec:
	src/TermRecord -s examples/test.ttyrec -b ttyrec \
				   -m templates/static.jinja2 \
				   -d 30 500 \
				   -o examples/ttyrec-static.html

clean:
	rm ${DYNAMIC_OBJS} ${STATIC_OBJS} 
