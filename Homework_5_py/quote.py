from colorama import init, Fore, Style


def quote():
    init()
    quote = f"{Fore.LIGHTBLACK_EX}\"Don't compare yourself with anyone in this world…\n{Style.RESET_ALL}{Fore.RED}if{Style.RESET_ALL} you {Fore.RED}do so{Style.RESET_ALL}, you are insulting yourself.{Fore.LIGHTBLACK_EX}\"\n{Style.RESET_ALL}- Bill Gates"
    print(quote)

quote()