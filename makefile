
# REDIGER DENNE VARIABELEN
ZIP_NAME = navn-på-spillet.zip

# variable to exclude files and folders from the zip file
EXCLUDE = ".git/*" ".git/**" "*.zip" "makefile" "__pycache__/*" "__pycache__/**" "venv/*" "venv/**"

.PHONY: zip

zip:
	zip -r $(ZIP_NAME) . -x $(EXCLUDE)
