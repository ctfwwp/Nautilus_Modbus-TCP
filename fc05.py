#fuction code = 05

ctx.rule("START", "{MBAP}{PDU}\n")   

ctx.rule("MBAP", "{Tid}{Pid}00{Length}{Uid}")

ctx.script("Length", ["Len"], lambda leng:'{:02x}'.format(len(leng)//2))

ctx.rule("Len", "{Uid}{PDU}")

ctx.rule("PDU", "{FC}{Data}")

ctx.rule("Tid", "{Byte}{Byte}")

ctx.rule("Pid", "0000")

ctx.rule("Uid", "01")

ctx.rule("FC", "05")

ctx.rule("Data", "{Data_addr}{SET_value}")

ctx.script("Data_addr", ["Byte1"], lambda num: str('{:04X}'.format(int(num))))

ctx.regex("Byte1", "(?:[0-9]|[1-9][0-9]|[1-3][0-9]{2}|40[0-8][0-9]|409[0-6])")

ctx.rule("SET_value", "FF00")

ctx.rule("SET_value", "0000")

ctx.rule("SET_value", "FF{Byte}")

ctx.rule("SET_value", "{Byte}00")

ctx.rule("SET_value", "00{Byte}")

ctx.regex("Byte", "(?:[0-9A-F]{2}|[0-9a-f]{2})|(?:[0-9A-F]{2}|[0-9a-f]{2})")