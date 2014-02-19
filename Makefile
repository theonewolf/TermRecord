DYNAMIC_OBJS	=	examples/figlet-dynamic.html examples/gcc-dynamic.html \
				    examples/htop-dynamic.html
STATIC_OBJS		=	examples/figlet-static.html examples/gcc-static.html \
				    examples/htop-static.html
DYN_DEP			=	templates/dynamic.jinja2 templates/base.jinja2
STATIC_DEP		=	templates/static.jinja2 templates/base.jinja2

default: dynamic static
dynamic: ${DYNAMIC_OBJS}
static: ${STATIC_OBJS}

examples/%-dynamic.html: ${DYN_DEP} examples/%.time examples/%.script
	src/jTermReplay.py examples/${*F}.script examples/${*F}.time \
				       templates/dynamic.jinja2 examples/${*F}-dynamic.html

examples/%-static.html: ${STATIC_DEP} examples/%.time examples/%.script
	src/jTermReplay.py examples/${*F}.script examples/${*F}.time \
				       templates/static.jinja2 examples/${*F}-static.html

clean:
	rm ${DYNAMIC_OBJS} ${STATIC_OBJS} 
