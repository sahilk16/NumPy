{
 "metadata": {
  "name": ""
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "\n",
      "%pylab\n",
      "\n",
      "\n",
      "''' Matplotlib basics\n",
      "\n",
      "normal plot - using red circles(we put \"r-o\" in the plot function to use red dots)\n",
      "diff examples - \"b-o\"- blue colour with circles\n",
      "              - \"r-^\" - red colour with triangles and so on..\n",
      "              - different colours are green - \"g\", Cyan - \"c\", Magenta = \"m\" etc\n",
      "                 '''\n",
      "\n",
      "x = linspace(0, 2 * pi, 40)\n",
      "y = sin(x)\n",
      "\n",
      "plot(x,y, 'r-o')\n",
      "\n",
      "'''normal scattered plot - we use a scatter function which helps us to scatter the plot'''\n",
      "\n",
      "x = linspace(0, 2 * pi, 40)\n",
      "y = sin(x)\n",
      "\n",
      "scatter(x,y)\n",
      "\n",
      "\n",
      "''' colored scatter plot with a color bar '''\n",
      "\n",
      "x = rand(2000)\n",
      "y = rand(2000)\n",
      "size = rand(200) * 3\n",
      "color = rand(200)\n",
      "\n",
      "scatter(x, y, size, color)\n",
      "colorbar()\n",
      "\n",
      "''' plotting subplots - here we make use of subplot which has attributes - row, coloumn, active plot\n",
      "                        we can change the no of rows and coloumns as per our choice'''\n",
      "\n",
      "x = array([1, 2, 3, 4,1,3])\n",
      "y = array([2, 3,1,2,3])\n",
      "\n",
      "subplot(2, 1, 1)\n",
      "plot(x)\n",
      "\n",
      "subplot(2, 1, 2)\n",
      "plot(y)\n",
      "\n",
      "''' Adding labels, titles and grids to a plot'''\n",
      "\n",
      "x = array([2,2, 4, 5,6])\n",
      "y = array([3,4, 6, 7, 8])\n",
      "\n",
      "plot(x, y, label = 'number plotting')\n",
      "legend()\n",
      "title(numbers)\n",
      "grid()\n",
      "\n",
      "\n",
      "\n",
      "\n"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "Using matplotlib backend: TkAgg\n",
        "Populating the interactive namespace from numpy and matplotlib\n"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stderr",
       "text": [
        "WARNING: pylab import has clobbered these variables: ['size']\n",
        "`%pylab --no-import-all` prevents importing * from pylab and numpy\n"
       ]
      },
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 14,
       "text": [
        "[<matplotlib.lines.Line2D at 0x7f255b8c5210>]"
       ]
      }
     ],
     "prompt_number": 14
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}