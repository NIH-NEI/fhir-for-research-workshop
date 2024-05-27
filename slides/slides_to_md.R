rmarkdown::render("slides.qmd", output_format = rmarkdown::md_document(variant="gfm", pandoc_args="--wrap=none"), output_file = "slides.md")

