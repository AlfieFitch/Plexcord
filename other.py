    if message.content.startswith('Jacob'):
        await message.channel.send('Retard alert, am i right!')

    if message.content.startswith('?ye'):
        url= 'https://api.kanye.rest'
        r = requests.get(url)
        quote = json.loads(r.text)
        print ("New Kanye Quote coming up!")
        newquote = str(quote)
        newnewquote = newquote.replace('{', '')
        nextquote = newnewquote.replace(':', '')
        contquote = nextquote.replace("'", '')
        finalquote = contquote.replace("quote", '')
        finalfinalquote = finalquote.replace("}", '')
        await message.channel.send('Ye once said: ' + finalfinalquote)

    if message.content.startswith('?em'):
        await message.channel.send('Sorry, No one has created an API for this :(')

    #if message.content.startswith(''):

        #spell = Speller(lang='en')
       # correct = spell(message.content)

        #if correct != message.content:
         #   await message.channel.send("Uh Oh! Did you mean **" + correct + "** instead? Retard!")

    if message.content.startswith('?corona'):
        url = "https://covid-19-data.p.rapidapi.com/totals"

        headers = {
        'x-rapidapi-key': "70cc6370b5msh425aa65bcbe5e16p17ac44jsn78cb07a3d254",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        li = list(response.text.split(","))

        deaths = li[3]
        deaths = deaths.replace('"', ' ')
        deaths = deaths.replace('d', 'D')
        deaths = deaths.replace(':', '= ')
        await message.channel.send(deaths)