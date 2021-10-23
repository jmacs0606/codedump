exec = doge.ready
sources = ${wildcard src/*.c}
objects = ${sources:.c=.o}
flags = -g
$(exec): $(objects)
	gcc $(objects) $(flags) -o $(exec)
%.o: %.c include/%.h
	gcc -c $(flags) $< -o $@

install:
	make
	cp ./doge.ready /usr/local/bin/dogescript

clean:
	-rm *.ready
	-rm *.o
	-rm src/*.o

