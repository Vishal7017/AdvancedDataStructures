# define move_to_end() here
def move_to_end(package, gemstone):
  result = []
  if len(package) == 0:
    return []
  
  if package[0] == gemstone:
    result += move_to_end(package[1:],gemstone)
    result.append(package[0])
  
  else:
    result.append(package[0])
    result += move_to_end(package[1:],gemstone)
  return result
  

  

# Test code - do not edit
gemstones = ["Amber", "Sapphire", "Amber", "Jade"]
print(move_to_end(gemstones, "Amber"))