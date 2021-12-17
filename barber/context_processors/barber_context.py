from barber.forms import NewsLetterForm


def add_newsletter_form(request):
    newsletter_form = NewsLetterForm()
    return {
        'news_letter_form': newsletter_form
    }