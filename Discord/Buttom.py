'''
I hope my tools can help you!
Please don't pretend to be the creator, but you don't have to say who created it, just enjoy!

** Necessary **
Discord.py recent lib
'''
#imports
try:
  import discord
  from discord.ext import commands
except:
  import os
  os.system('pip install discord.py')
  import discord
  from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '.', intents = intents)

# Make buttons 
class Button(discord.ui.View):
  def __init__(self):
    # Timout is to declare the time at which the Button can be clicked.
    super().__init__(timout= 300)
 # The decorator is for the interaction function to be declared as a button interaction.
  @discord.ui.Buttom(label = 'Say Hello', style= discord.ButtonStyle.blurple, emoji= '👋')
  async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message(content = 'Hi! 👋')

# Make embeds and use button. (Using Tree Comands Method)
@bot.tree.command(name = 'hi', description = 'say `hi` for me')
async def hi(interaction: discord.Interaction):
  # Create a object for embed
  embed = discord.Emned(title = '🎉 Hello Systen', description = 'Say hello for me using the button')
  # set footer 
  #embed.set_footer(text= 'text', url= 'url')
  embed.set_footer(text = 'Use the button')
  #set image
  #embed.set_image(url= 'url_image')
  await interaction.response.send_messagd(content = '@everyone', embed = embed, view= view)
