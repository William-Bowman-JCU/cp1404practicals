import wikipedia

title = input('Enter page title: ').strip()
while title != '':
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.summary.split('\n')[0])
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as DisambiguationError:
        print('We need a more specific title. Try one of the following, or a new search:')
        print(DisambiguationError.options)
    except wikipedia.exceptions.PageError as PageError:
        print(PageError)
    title = input('\nEnter page title: ').strip()