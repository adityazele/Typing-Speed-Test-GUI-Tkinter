# similar service https://typing-speed-test.aoeu.eu/ (Business)

from tkinter import *
from tkinter import ttk

paragraph = '''In the digital age, information flows seamlessly across the vast expanse of the internet. The speed of
communication has reshaped how we connect, share, and collaborate. Social media platforms amplify our voices, creating a
global conversation. However, amidst the virtual chatter, privacy concerns linger, prompting debates on data protection
and online security. Technological advancements continue to redefine industries. Automation and artificial intelligence
streamline processes, but questions about job displacement arise. The balance between innovation and ethical
considerations is delicate. As we navigate this dynamic landscape, the need for digital literacy and critical
thinking becomes increasingly apparent.'''

modified_paragraph = paragraph.replace('\n', ' ')


def match_text(event):
    global pos
    if not (event.keysym.startswith('Shift') or event.keysym == 'Caps_Lock'):
        typed_text = type_box.get('1.0', 'end-1c')
        if typed_text[-1] == ' ':
            space()
        else:
            if len(typed_text) <= len(original_text[char]):
                if original_text[char][len(typed_text)-1] == typed_text[-1]:
                    text_box.tag_add('correct', f'1.{pos}')
                    text_box.tag_config('correct', foreground='green')
                    print(f'1.{pos} is colored green')
                else:
                    text_box.tag_add('wrong', f'1.{pos}')
                    text_box.tag_config('wrong', foreground='red')
                    print(f'1.{pos} is colored red')
                pos += 1


def space():
    global char, total_len, pos_l, pos_u, pos
    type_box.delete('1.0', 'end-1c')
    text_box.tag_remove('highlight', f'1.{pos_l}', f'1.{pos_u}')
    char += 1
    total_len += len(original_text[char-1]) + 1
    pos_l = total_len
    pos = pos_l
    highlight_text()


def highlight_text():
    global pos_u
    text = original_text[char]
    pos_u = total_len + len(original_text[char])
    text_box.tag_add('highlight', f'1.{pos_l}', f'1.{pos_u}')
    text_box.tag_config('highlight', background='yellow')
    highlighted_text = text_box.get(f'1.{pos_l}', f'1.{pos_u}')
    print(f'{highlighted_text} [1.{pos_l} - 1.{pos_u}] is highlighted')


root = Tk()
root.title('Typing Speed Test')

frm = ttk.Frame(root, padding=10)
frm.grid()

text_box = Text(frm, wrap=WORD, width=70, height=11)
text_box.insert('1.0', modified_paragraph)
text_box.grid(row=0, column=0)

original_text = text_box.get('1.0', 'end-1c').split()

char = 0
pos_l = 0
pos_u = 0
pos = 0
total_len = 0
highlight_text()

type_box = Text(frm, width=70, height=1)
type_box.grid(row=1, column=0)
type_box.bind('<KeyRelease>', match_text)

root.mainloop()

