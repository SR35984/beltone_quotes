from __future__ import unicode_literals
from django.db import models

class QuoteManager(models.Manager):
	def validate(self, form_data):
		errors = []

		if len(form_data['quoted_by']) == 0:
			errors.append("Quoted by???")
		
		if len(form_data['message']) == 0:
			errors.append("Please type in quote!")

		return errors

	def create_quote(self, form_data):
		return self.create(
			quoted_by=form_data['quoted_by'],
			message=form_data['message'],
			)

class Quote(models.Model):
	quoted_by = models.CharField(max_length=150)
	message = models.CharField(max_length=150)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = QuoteManager()