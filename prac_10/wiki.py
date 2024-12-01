import wikipedia

MAX_SENTENCES = 3
title = input('Enter page title: ').strip()
while title != '':
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        # As to not make an unnecessary wikipedia.summary API call, this is how I limited the amount of sentences shown from the summary property. 
        # The only weakness I could find is if there is a decimal number if the sentences
        print('.'.join(page.summary.split('.')[:MAX_SENTENCES]) + '.')
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as DisambiguationError:
        print('We need a more specific title. Try one of the following, or a new search:')
        print(DisambiguationError.options)
    except wikipedia.exceptions.PageError as PageError:
        print(PageError)
    title = input('\nEnter page title: ').strip()