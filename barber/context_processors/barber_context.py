from barber.forms import NewsLetterForm


def add_newsletter_form(request):
    return {'news_letter_form': NewsLetterForm()}