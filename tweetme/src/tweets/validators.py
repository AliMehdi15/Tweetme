
from django.core.exceptions import ValidationError

def validate_content(value):
	content = value
	if content == "":
		raise ValidationError("Fuck You, Don't be silly and write something!!!! Don't leave it fucking blank")
	return value