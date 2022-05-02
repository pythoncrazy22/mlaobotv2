import discord
from discord.ext import commands
import oeispy as op

class oeis(commands.Cog, name="Oeis commands"):
	'''These are the oeis commands'''

	def __init__(self, bot):
		self.bot = bot

#----------------------------------------------------------------
	async def cog_check(self, ctx):  
		'''
		The default check for this cog whenever a command is used. Returns True if the command is allowed.
		'''
		return ctx.author.id == self.bot.author_id

#----------------------------------------------------------------
	@commands.command(require_var_positional=True,name='sequence',aliases=['seq'])  
	async def sequence(self, ctx,*numbers):
		'''
		Prints out the oeis sequence given certain numbers
		Example usage:
		sequence 1 1 2 3 5 8 13
		'''
		num = ''.join(numbers)
		result = op.resultEois(num)
		number_results=op.countResult(result)
		sequence_oeis=op.topResult(result)
		embedVar = discord.Embed(title="The sequence", description="From OEIS", color=0x738ad7)
		embedVar.add_field(name="Number of Results", value=number_results, inline=True)
		embedVar.add_field(name="Name", value=sequence_oeis["name"], inline=True)
		embedVar.add_field(name="OEIS Number", value=sequence_oeis["number"], inline=True)
		embedVar.add_field(name="Terms", value=sequence_oeis["data"], inline=True)
		embedVar.set_footer(text="mlao nerd")
		await ctx.send(embed=embedVar)
		print("done")


		


def setup(bot):
	bot.add_cog(oeis(bot))