
class Strings():

	def hostname(name):
		addName = "Net"
		if name:
			addName = name
		
		host = "\r[Quantum@" + addName + "]══► $ "
		return host

	MainColors = {
		"Red": "\e[31m",
		"Yellow": "\e[33m",
		"Blue": "\e[34m",
		"Purple": "\e[35m",
		"Green": "\e[32m",
		"Cyan": "\e[36m",
		"Black": "\e[30m",
		"Grey": "\e[37m",
		"White": "\e[37m",
		"Reset": "\e[39m",
		"Background_Red": "\e[41m",
		"Background_Green": "\e[42m",
		"Background_Yellow": "\e[43m",
		"Background_Blue": "\e[44m",
		"Background_Purple": "\e[45m",
		"Background_Cyan": "\e[46m",
		"Background_LightGrey": "\e[47m",
		"Background_DarkGrey": "\e[100m",
		"Background_LightRed": "\e[101m",
		"Background_LightGreen": "\e[102m",
		"Background_LightYellow": "\e[103m",
		"Background_Reset": "\e[49m",
		"Clear": "\033[2J\033[1;1H"
	}
