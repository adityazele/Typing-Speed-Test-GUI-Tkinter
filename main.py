# similar service https://typing-speed-test.aoeu.eu/ (Business)

from tkinter import *
from tkinter import ttk, messagebox

paragraph = '''In the digital age, information flows seamlessly across the vast expanse of the internet. The speed of
communication has reshaped how we connect, share, and collaborate. Social media platforms amplify our voices, creating a
global conversation. However, amidst the virtual chatter, privacy concerns linger, prompting debates on data protection
and online security. Technological advancements continue to redefine industries. Automation and artificial intelligence
streamline processes, but questions about job displacement arise. The balance between innovation and ethical
considerations is delicate. As we navigate this dynamic landscape, the need for digital literacy and critical
thinking becomes increasingly apparent.'''

modified_paragraph = paragraph.replace('\n', ' ')


def match_text(event):
    global pos, correct, wrong, first_key

    if not (event.keysym.startswith('Shift') or event.keysym == 'Caps_Lock'):
        if first_key:
            first_key = False
            start_timer()
        typed_text = type_box.get('1.0', 'end-1c')
        if typed_text[-1] == ' ':
            space()
        else:
            if len(typed_text) <= len(original_text[char]):
                if original_text[char][len(typed_text)-1] == typed_text[-1]:
                    text_box.tag_add('correct', f'1.{pos}')
                    text_box.tag_config('correct', foreground='green')
                    print(f'1.{pos} is colored green')
                    correct += 1
                else:
                    text_box.tag_add('wrong', f'1.{pos}')
                    text_box.tag_config('wrong', foreground='red')
                    print(f'1.{pos} is colored red')
                    wrong += 1
                pos += 1


def space():
    global char, total_len, pos_l, pos_u, pos
    type_box.delete('1.0', 'end-1c')
    text_box.tag_remove('highlight', f'1.{pos_l}', f'1.{pos_u}')
    char += 1
    total_len += len(original_text[char-1]) + 1
    print(total_len)
    pos_l = total_len
    pos = pos_l
    if char < total_char:
        highlight_text()
    else:
        messagebox.showinfo('Test Complete', f'Congratulations! Your typing test is complete\n correct: {correct} wrong: {wrong}')
        root.quit()


def highlight_text():
    global pos_u
    text = original_text[char]
    pos_u = total_len + len(original_text[char])
    text_box.tag_add('highlight', f'1.{pos_l}', f'1.{pos_u}')
    text_box.tag_config('highlight', background='yellow')
    highlighted_text = text_box.get(f'1.{pos_l}', f'1.{pos_u}')


def start_timer():
    t = int(time_box.get('1.0', 'end-1c'))
    if t > 0:
        time_box.delete('1.0', 'end-1c')
        time_box.insert('1.0', f'{t-1}')
        root.after(1000, start_timer)
    else:
        messagebox.showinfo('Test Complete', f'Congratulations! Your typing test is complete\n correct: {correct} wrong: {wrong}')
        root.quit()


root = Tk()
root.title('Typing Speed Test')

frm = ttk.Frame(root, padding=10)
frm.grid()

time_label = Label(frm, text='time left')
time_label.grid(row=0, column=0, padx=(0,40))

time_box = Text(frm, width=2, height=1)
time_box.grid(row=0, column=0, padx=(40, 0))
time_box.insert('1.0', '60')

text_box = Text(frm, wrap=WORD, width=70, height=11)
text_box.insert('1.0', modified_paragraph)
text_box.grid(row=1, column=0)

original_text = text_box.get('1.0', 'end-1c').split()

char = 0
pos_l = 0
pos_u = 0
pos = 0
total_len = 0
correct = 0
wrong = 0
first_key = True
total_char = len(original_text)
highlight_text()

type_box = Text(frm, width=70, height=1)
type_box.grid(row=2, column=0)
type_box.bind('<KeyRelease>', match_text)

root.mainloop()

