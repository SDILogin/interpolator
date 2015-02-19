import tkinter
import math, random

class WindowManager(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title('simple interpolator')

        self.canvas = tkinter.Canvas(self, width = 1300, height = 300)
        self.canvas.pack()

        self.btn_generate = tkinter.Button(self, text="regenerate")
        self.btn_generate.pack(side = tkinter.BOTTOM)
        self.btn_generate.bind('<Button-1>', self.generate_new_sequence)

    def draw_plot(self, table):
        interpolated_table = self.interpolation(self.interpolation2(self.interpolation2(table)))
        for i in range(0, len(interpolated_table) -2, 2):
            color = 'green'
            if interpolated_table[i + 1] < interpolated_table[i + 3]:
                color = 'red'
            self.canvas.create_line(
                interpolated_table[i], interpolated_table[i+1],
                interpolated_table[i+2], interpolated_table[i+3],
                fill=color)
        self.canvas.create_line(*table, fill='black')

    def interpolation(self, table, count = 3):
        res = table[:]
        for _ in range(count):
            nres = []
            for ind in range(0, len(res) - 2, 2):
                nres.append(res[ind])
                nres.append(res[ind+1])
                nres.append(res[ind] / 2 + res[ind + 2] / 2)
                nres.append(res[ind+1] /2 + res[ind + 3] / 2)
                nres.append(res[ind+2])
                nres.append(res[ind+3])
            res = nres[:]
        return res

    def interpolation2(self, table):
        res = table[:]
        for i in range(0, len(res) -4, 2):
            res[i + 2] = res[i] /3 + res[i+2]/3 + res[i + 4] /3 
            res[i + 3] = res[i+1]/3 + res[i+3]/3 + res[i+5] /3
        return res 

    def generate_new_sequence(self, *arg, **kword):
        self.canvas.delete(tkinter.ALL)
        x = 0
        xa = []
        while x < 2 * 3.1415:
            xa.append(x)
            x+= 0.1

        xy = []
        for x in xa:
            xy.append(50 + x * 190)
            xy.append(math.sin(x * random.random()) * 50 + 100)    
        self.draw_plot(xy)


if __name__ == '__main__':
    wm = WindowManager()
    wm.generate_new_sequence()
    wm.mainloop()