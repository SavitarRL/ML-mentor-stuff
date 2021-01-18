import random
import matplotlib.pyplot as plt
import math as m
x=[(0,0),(1,0),(0,1),(1,1)]
y=[1,0,0,1]




class Model:
  def __init__(self):
    self.w = [random.gauss(0,2),random.gauss(0,2)] 
    self.b = random.gauss(0,2)
    
  def f(self,x):
    output = self.activation(self.w[0]*x[0] + self.w[1]*x[1] +self.b)
    return output
  def activation(self,x):
      return 1/(1+m.exp(-x))

  def descent(self,gradients,learning_rate=0.01):
    self.w[0] -= learning_rate*gradients[0]
    self.w[1] -= learning_rate*gradients[1]
    self.b -= learning_rate*gradients[2]
    
  def intercept(self,x0):
    return self.w[0]*x0/-self.w[1] + self.b/-self.w[1]

    
##plotting
def plot():
  for i in range(len(x)):
    plt.scatter(x[i][0],x[i][1],color="r" if y[i]==0 else "b")

plt.ion()
plt.show()


model = Model()
epochs = 100
plot_x = range(0,10,9)
for i in range(epochs):
  order = list(range(len(x)))
  random.shuffle(order)
  for j in order:
    data = x[j]
    answer = y[j]
    output = model.f(data)
    print("Answer {}".format(answer))
    print("Output {}".format(output))
    loss = (output-answer)**2
    dloss_dw1 = 2.0*(data[0])*(output - answer)
    dloss_dw2 = 2.0*(data[1])*(output - answer)
    dloss_db = 2.0*(output - answer)
    model.descent([dloss_dw1,dloss_dw2,dloss_db],learning_rate=0.01)
    ##plotting
    plot_y = [model.intercept(xs) for xs in plot_x]
    plt.cla()
    plt.plot(plot_x,plot_y)
    plot()
    plt.pause(0.02)

  print(model.w)
  


