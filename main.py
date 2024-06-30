# Приложение для отслеживания расходов:
# Описание: Программа для учета личных финансов, с возможностью ввода расходов и доходов,
# а также построения графиков.
import pathlib
from tkinter import *
import matplotlib.pyplot as plt


def write_in_file(*data):
    coint, action, path_file, list_ = data
    if coint != '':
        try:
            if float(coint) > 0:
                if action == 'credit':
                    coint = '-' + coint
                elif action == 'debet':
                    coint = coint
                list_.append(coint)
                with open(file=path_file, mode='a', encoding='utf-8') as file:
                    file.write(coint + '\n')

            label.config(text='')
        except ValueError:
            label.config(text='Необходимо ввести число')
        finally:
            sum_balans(list_data)


def sum_balans(lst):
    balans = 0
    for x in lst:
        balans += float(x)

    balans_lbl.config(text=f'На балансе: {balans:.2f} руб.')


def graf_view(*lst_):
    lst_d, flag = lst_
    deb_list = list()
    cre_list = list()
    for value in lst_d:
        if float(value) < 0:
            cre_list.append(float(value))
        elif float(value) > 0:
            deb_list.append(float(value))
        else:
            pass
    if flag == 'debet':
        x = [a for a in range(len(deb_list))]
        y = deb_list
        plt.title('График поступления денег')
    elif flag == 'credit':
        x = [a for a in range(len(cre_list))]
        y = cre_list
        plt.title('График расхода денег')

    plt.plot(x, y, 'o-r', alpha=0.7, label='first', lw=5, mec='b', mew=2, ms=10)
    plt.grid()
    # plt.draw()
    plt.show()


file_name = 'file.csv'
path = pathlib.Path.cwd() / file_name
if not path.exists():
    path.touch()

list_data = list()

with open(file=path, mode='r', encoding='utf-8') as f:
    r = f.readlines()
    for v in r:
        if v != '\n':
            list_data.append(v[:-1])


root = Tk()
root.title("Программа для учета личных финансов")
root.geometry("800x250")
frame1 = Frame(root, padx=10, pady=10, border=1, relief=SOLID, height=300)
frame1.pack(fill=X)

method_lbl = Label(frame1, text="Выберите операцию:", font=36)
method_lbl.grid(row=1, column=1)

var = StringVar()
var.set("credit")
credit_rdb = Radiobutton(frame1, text='Расход', variable=var, value="credit", font=36)
debet_rdb = Radiobutton(frame1, text='Приход', variable=var, value="debet", font=36)
credit_rdb.grid(row=1, column=2)
debet_rdb.grid(row=1, column=3)

enter = Entry(frame1)
enter.grid(row=3, column=1)

calc_btn = Button(frame1, text="Ввести сумму", command=lambda: (write_in_file(enter.get(), var.get(), path, list_data),
                                                                enter.delete(0, END)))
calc_btn.grid(row=3, column=2)

label = Label(frame1, text='', font=36)
label.grid(row=3, column=5)

balans_lbl = Label(frame1, text='')
balans_lbl.grid(row=3, column=6)
sum_balans(list_data)

frame2 = Frame(root, padx=10, pady=10, border=2, relief=RAISED)
frame2.pack(fill=X)


graf_btn = Button(frame2, text="Показать график Прихода", command=lambda: graf_view(list_data, 'debet'))
graf_btn.grid(row=3, column=2)

graf_btn2 = Button(frame2, text="Показать график Расхода", command=lambda: graf_view(list_data, 'credit'))
graf_btn2.grid(row=3, column=3)

root.mainloop()

