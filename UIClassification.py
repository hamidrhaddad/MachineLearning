from tkinter import  *
from tkinter.ttk import Combobox
Form = Tk()
Form.geometry('800x600')

R2Value = StringVar()
txtModel = StringVar()

def NewData():
    from sklearn.datasets import make_blobs
    x, y = make_blobs(n_samples=1000, n_features=2, centers=3)
    global z1
    global z2
    z1 = x
    z2= y
def NewDataMoon():
    from sklearn.datasets import make_moons
    x, y = make_moons(n_samples=1000)
    global z1
    global z2
    z1 = x
    z2= y
def NewDataCircle():
    from sklearn.datasets import make_circles
    x, y = make_circles(n_samples=1000)
    global z1
    global z2
    z1 = x
    z2= y
def Action():
    x = z1
    y = z2
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    from sklearn.naive_bayes import GaussianNB
    model2 = txtModel.get()
    match model2:
        case 'MLPClassifier':
            model = MLPClassifier()
        case 'DecisionTreeClassifier':
            model = DecisionTreeClassifier()
        case 'SVM':
            model = SVC(kernel='linear')
        case 'Naive_bayes':
            model = GaussianNB()

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.33)
    model.fit(xtrain, ytrain)
    r = model.score(xtest, ytest)
    ypred = model.predict(xtest)
    R2Value.set(r)
    global  z3
    global z4
    global z5
    z3 = xtrain
    z4 = ytrain
    z5 = model


def plot():
    import matplotlib.pyplot as plt
    from mlxtend.plotting import plot_decision_regions
    plot_decision_regions(z3,z4, clf = z5)
    plt.show()

frame = LabelFrame(Form)

label1 = Label(frame , text='Generate Linear Data')
label1.grid(row=0 , column = 0, padx = 10, pady = 10)

GenerateButton = Button(frame, text="Enter For Data Linear Generation Randomly", width=40, command= NewData)
GenerateButton.grid(row=1, column =0, padx = 15, pady=15)

label12 = Label(frame , text='Generate moon Data')
label12.grid(row=2 , column = 0, padx = 10, pady = 10)

GenerateButton2 = Button(frame, text="Enter For Data moon Generation Randomly", width=40, command= NewDataMoon)
GenerateButton2.grid(row=3, column =0, padx = 15, pady=15)

label13 = Label(frame , text='Generate Circle Data')
label13.grid(row=4 , column = 0, padx = 10, pady = 10)

GenerateButton3 = Button(frame, text="Enter For Data Circle Generation Randomly", width=40, command= NewDataCircle)
GenerateButton3.grid(row=5, column =0, padx = 15, pady=15)

label14 = Label(frame , text='Select Method')
label14.grid(row=6 , column = 0, padx = 10, pady = 10)

entModel = Combobox(frame, width=20, textvariable= txtModel, state= 'readonly' )
entModel.grid(row=7, column= 0, padx=15, pady =15)
entModel['values']= ['MLPClassifier', 'DecisionTreeClassifier', 'SVM', 'Naive_bayes']

frame.place(x=20, y=20)

frame2 = LabelFrame(Form)

ActioneButton = Button(frame2, text="Enter For implementation", width=35, command= Action)
ActioneButton.grid(row=0, column =0, padx = 15, pady=15)

label2 = Label(frame2, text='R2 Value')
label2.grid(row=1 , column = 0, padx = 10, pady = 10)

entryR2 = Entry(frame2, textvariable= R2Value, width=10)
entryR2.grid(row=2, column=0 , padx =10, pady=10)

label3 = Label(frame2, text='Plot Diagram')
label3.grid(row=3 , column = 0, padx = 10, pady = 10)

DiagramButton = Button(frame2, text="Enter For Plotting", width=35, command= plot)
DiagramButton.grid(row=4, column =0, padx = 10, pady=10)

frame2.place(x=450, y= 20)

Form.mainloop()