SRC = $(basename $(wildcard *.tex))
MF_FILES = $(wildcard *.mf)

all:
	$(MAKE) -i tex
	$(MAKE) bib
	$(MAKE) mf
	$(MAKE) tex
	$(MAKE) tex


tex:
	pdflatex $(SRC)


bib:
	bibtex $(SRC)

mf:
	for file in $(MF_FILES); do \
		mf "\mode=localfont; input $$file;"; \
	done


RM = $(sort $(wildcard *.dvi *.log *.aux *.600pk *.600gf *.mf *.t1 *tfm  annihilation1* annihilation2 *~))

clean:
	rm -r $(RM)

cleanAll:
	$(MAKE) clean
	rm -rf *.pdf
	rm -rf *bbl
	rm -rf *blg

test:
	echo $(SRC)