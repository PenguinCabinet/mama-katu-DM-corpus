
text=""
with open("in_conv.txt","r",encoding="utf-8") as f:
    text=f.read()

text=text.replace("\n","__br__")

out_text=""
with open("data.txt","r",encoding="utf-8") as f:
    for line in f:
        if not line.isspace():
            out_text+=line

if out_text=="" or out_text[len(out_text)-1]=="\n":
    out_text+=text
else:
    out_text+="\n"+text
with open("data.txt","w",encoding="utf-8") as f:
    f.write(out_text)
