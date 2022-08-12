from tkinter import *
from PIL import ImageTk, Image
import os
import random

root = Tk()
geo1 = '680x330'
geo2 = '630x390'
root.geometry(geo1)
root.title('Cree Syllabic Image Game')
root.iconbitmap(r"Icon\CrowIcon.ico")
imagen = 'Start.png'

image_list = []
image_listgame = []
button_list=[]
click_count = 0
correct_index = 0
current_click = ''
correct_answers = 0
second_click_count = 0
game_choice = 0

font_tuple = ('Euphemia', 11, 'bold')




# function to generate correct images for buttons (1 correct 3 randoms)
def button_image_gen():
    global button_list
    global correct_index
    button_list = []
    m_list = []
    for file in os.listdir('Images'):
        m_list.append(file)

    # remove correct answer from master list
    m_list.remove(imagen)
    m_list.remove('Start.png')
    # add 3 random image names to button list
    button_list.append(m_list.pop(random.randrange(len(m_list))))
    button_list.append(m_list.pop(random.randrange(len(m_list))))
    button_list.append(m_list.pop(random.randrange(len(m_list))))
    # append correct answer randomly
    button_list.insert(random.randint(0, len(button_list)), imagen)
    #store index of correct answer
    correct_index = button_list.index(imagen)



#function to display a second screen with previous questions answer
def second_screen():
    global button1
    global button2
    global button3
    global button4
    global scorecard
    global correct_answers
    global second_click_count
    global root

    #increment second click count
    second_click_count += 1
    #handle buttons for answer - disable all but correct
    if correct_index == 0:
        button2.destroy()
        button2 = Button(root, image=butt2_img, command=lambda: change_screen(), state=DISABLED)
        button2.grid(row=2, column=1)
        button3.destroy()
        button3 = Button(root, image=butt3_img, command=lambda: change_screen(), state=DISABLED)
        button3.grid(row=3, column=0)
        button4.destroy()
        button4 = Button(root, image=butt4_img, command=lambda: change_screen(), state=DISABLED)
        button4.grid(row=3, column=1)
    elif correct_index == 1:
        button1.destroy()
        button1 = Button(root, image=butt1_img, command=lambda: change_screen(), state=DISABLED)
        button1.grid(row=2, column=0)
        button3.destroy()
        button3 = Button(root, image=butt3_img, command=lambda: change_screen(), state=DISABLED)
        button3.grid(row=3, column=0)
        button4.destroy()
        button4 = Button(root, image=butt4_img, command=lambda: change_screen(), state=DISABLED)
        button4.grid(row=3, column=1)
    elif correct_index == 2:
        button1.destroy()
        button1 = Button(root, image=butt1_img, command=lambda: change_screen(), state=DISABLED)
        button1.grid(row=2, column=0)
        button2.destroy()
        button2 = Button(root, image=butt2_img, command=lambda: change_screen(), state=DISABLED)
        button2.grid(row=2, column=1)
        button4.destroy()
        button4 = Button(root, image=butt4_img, command=lambda: change_screen(), state=DISABLED)
        button4.grid(row=3, column=1)
    else:
        button1.destroy()
        button1 = Button(root, image=butt1_img, command=lambda: change_screen(), state=DISABLED)
        button1.grid(row=2, column=0)
        button2.destroy()
        button2 = Button(root, image=butt2_img, command=lambda: change_screen(), state=DISABLED)
        button2.grid(row=2, column=1)
        button3.destroy()
        button3 = Button(root, image=butt3_img, command=lambda: change_screen(), state=DISABLED)
        button3.grid(row=3, column=0)

    scorecard.destroy()
    #handle answer and update scorecard
    if int(current_click) == correct_index:
        #increment current score
        correct_answers += 1
        #create new scorecard
        scorecard = Label(score_frame,text=f'Your Answer was correct! \nNICE\n\nCURRENT SCORE: {correct_answers} out of {second_click_count}\n\n Click the correct answer to continue')
        scorecard.grid(row=0, column=1)
        scorecard.configure(font=font_tuple)
    else:

        scorecard = Label(score_frame, text=f'Your Answer was incorrect! \nNOT SO NICE\n\nCURRENT SCORE: {correct_answers} out of {second_click_count}\n\n Click the correct answer to continue')
        scorecard.grid(row=0, column=1)
        scorecard.configure(font=font_tuple)

#function that handles button clicks on the main 4
def answer_click():
    global button1
    global button2
    global button3
    global button4
    global butt1_label
    global butt1_img
    global butt2_label
    global butt3_label
    global butt4_label
    global butt2_img
    global butt3_img
    global butt4_img
    global button_list
    global choice1
    global choice2
    global choice3
    global choice_frame
    global image_frame

    image_frame.destroy()
    choice1.destroy()
    choice2.destroy()
    choice3.destroy()
    choice_frame.destroy()
    # destory old buttons
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()

    #change buttons
    butt1_img = PhotoImage(file = f'ImageSyllabics/{button_list[0]}')
    butt1_label = Label(image=butt1_img)
    button1 = Button(root, image=butt1_img, command=lambda m='0': change_screen(m))
    button1.grid(row=2, column=0)

    butt2_img = PhotoImage(file=f'ImageSyllabics/{button_list[1]}')
    butt2_label = Label(image=butt2_img)
    button2 = Button(root, image=butt2_img, command=lambda m='1' : change_screen(m))
    button2.grid(row=2, column=1)

    butt3_img = PhotoImage(file = f'ImageSyllabics/{button_list[2]}')
    butt3_label = Label(image = butt3_img)
    button3 = Button(root, image=butt3_img, command=lambda m='2': change_screen(m))
    button3.grid(row=3, column=0)

    butt4_img = PhotoImage(file = f'ImageSyllabics/{button_list[3]}')
    butt4_label = Label(image = butt4_img)
    button4 = Button(root, image=butt4_img, command=lambda m='3': change_screen(m))
    button4.grid(row=3, column=1)


#main function for changing screen on button click
def change_screen(button_press):
    global image_list
    global imagen
    global img_label
    global image1
    global click_count
    global current_click
    global scorecard
    global root

    root.geometry(geo2)
    #store click
    current_click = button_press
    # increment click counter
    click_count += 1
    #user click button index -
    if click_count % 2 != 0 and click_count < game_choice * 2 + 1:

        #forget the label for image
        img_label.grid_forget()

        #pop off next image from list

        imagen = image_listgame.pop()
        # generate buttons
        button_image_gen()
        #redefine image
        image1 = ImageTk.PhotoImage(Image.open(f'Images/{imagen}'))
        img_label = Label(image=image1)
        img_label.grid(row=0, column=0, sticky = W, padx = 15)
        #new scorecard
        scorecard.destroy()
        scorecard = Label(score_frame,text=f'CURRENT SCORE: {correct_answers} out of {second_click_count}')
        scorecard.grid(row=0, column=1)
        scorecard.configure(font=font_tuple)
        #generate new buttons
        answer_click()

    elif click_count % 2 == 0 and click_count < game_choice * 2 + 1:
        second_screen()
    else:
        final_screen()


def final_screen():
    global button1
    global button2
    global button3
    global button4
    global  scorecard
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    scorecard.destroy()
    #final scorecard
    scorecard = Label(score_frame, text=f'FINAL SCORE: {correct_answers} out of {second_click_count}\n\n Thanks for playing!')
    scorecard.grid(row=0, column=1)
    scorecard.configure(font=font_tuple)


#function that will handle the game selection
def choice_handler(button_press):
    global image_list
    global game_choice
    #update game choice
    game_choice = button_press
    # make list of images in directory of the correct length for game choice
    folder = "Images"
    if folder not in os.listdir():
        os.mkdir(folder)
    for file in os.listdir('Images'):
        image_list.append(file)

    # remove start image from list
    image_list.remove('Start.png')

    if button_press == 10:
            # reduce image list size to the choice
        for i in range(10):
            image_listgame.append(image_list.pop(random.randrange(len(image_list))))
        change_screen(1)
    elif button_press == 15:
        for i in range(15):
            image_listgame.append(image_list.pop(random.randrange(len(image_list))))
        change_screen(1)
    elif button_press == 20:
        for i in range(20):
            image_listgame.append(image_list.pop(random.randrange(len(image_list))))
        change_screen(1)


#create initial buttons
button1 = Button(root, command=lambda m='0': change_screen(m))

button2 = Button(root, command=lambda m='1' : change_screen(m))

button3 = Button(root, command=lambda m='2': change_screen(m))

button4 = Button(root, command=lambda m='3': change_screen(m))

image_frame = LabelFrame(root)
image_frame.grid(row=0, column=0, rowspan = 2)

#image label
image1 = ImageTk.PhotoImage(Image.open(f'Images/{imagen}'))
img_label = Label(image_frame, image = image1)
img_label.grid(row = 0, column = 0)

#score frame
score_frame = LabelFrame(root, padx = 20, pady = 30)
score_frame.grid(row=0, column=1, padx = 5, pady =20)

#score label
scorecard = Label(score_frame, text = f'Welcome to the game!\n\nClick the correct Syllabic to match the image\n\nGoodLuck!' )
scorecard.grid(row=0, column=1)
scorecard.configure(font = font_tuple)

#choice frame

choice_frame = LabelFrame(root, padx = 20, pady = 30, bd=0)
choice_frame.grid(row=1, column=1, padx = 5, pady =10)

#choice buttons
choice1 = Button(choice_frame, text = '10 questions', command = lambda m=10 : choice_handler(m))
choice1.grid(row=0, column = 0, pady = 15, padx = 5)
choice1.configure(font = font_tuple)

choice2 = Button(choice_frame, text = '15 questions', command = lambda m=15 : choice_handler(m))
choice2.grid(row=0, column = 1, pady = 15, padx = 5)
choice2.configure(font = font_tuple)

choice3 = Button(choice_frame, text = '20 questions', command = lambda m=20 : choice_handler(m))
choice3.grid(row=0, column = 2, pady = 15, padx = 5)
choice3.configure(font = font_tuple)

root.mainloop()