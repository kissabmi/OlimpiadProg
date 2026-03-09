all: help

clean:
	find . -type f \( -name "*.o" -o -name "*.a" -o -name "*.exe" -o -name "main" \) -delete
	@echo "Очистка завершена!"

help:
	@echo "Доступные команды:"
	@echo "  make clean  - удалить временные файлы компиляции"
	@echo "  make help   - показать эту справку"


.PHONY: all clean help
