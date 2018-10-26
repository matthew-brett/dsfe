.PHONY: help textbook clean serve bibliography

BIBLIOGRAPHIES= _data-science-bib/data_science.bib \
				_bibliography/course.bib

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  textbook    to convert the `notebooks/` folder into Jekyll markdown in `chapters/`"
	@echo "  clean       to clean out site build files"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"
	@echo "  serve       to serve the repository locally with Jekyll"

textbook:
	python scripts/generate_textbook.py

write-rmd:
	bash scripts/write_rmds.sh

runall:
	python scripts/execute_all_notebooks.py

check:
	# See: https://github.com/mwouts/jupytext/issues/95
	./scripts/check_jpts.sh

rebuild-notebooks:
	python scripts/rebuild_notebooks.py

bibliography: $(BIBLIOGRAPHIES)
	cat $(BIBLIOGRAPHIES) > _bibliography/references.bib

components: bibliography rebuild-notebooks textbook

build: components
	bundle exec jekyll build

github: build
	ghp-import -n _site -p -f

clean:
	python scripts/clean.py
	rm _bibliography/references.bib

ship: clean rebuild-notebooks textbook

# You need Ruby and Gem.  Then:
# gem install --user bundler jekyll
# # To avoid a compilation error for nokogiri
# bundle config build.nokogiri --use-system-libraries
# bundle install

serve: components
	bundle exec jekyll serve

make continuous-build:
	while true; do \
		(make rebuild-notebooks || tput bel) ; \
		sleep 5; \
	done
