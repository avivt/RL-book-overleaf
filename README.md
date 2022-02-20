# RL-book-overleaf

Reinforcement Learning: Foundations
book draft
By Shie Mannor, Yishay Mansour and Aviv Tamar

Guidelines for submitting corrections:

The main skeleton file is RL-book.tex.
The file defs.tex contains common notation and macros. 

The folder current_chapters is where the content is - this is where you can make changes.
Each chapter has its own .tex file; propose a change by making a pull request.

Important: please follow the notations in the files by using the macros that we already use (e.g., \state, \action, \Value). 
A few common ones appear below.

Please make sure there are no compilation errors for the changes you propose (by compiling the latex yourself on your machine or on overleaf).

For general git guidelines, see the guides here: https://guides.github.com/


Common Macros:

\newcommand{\mdp}{\mathcal{M}}
\newcommand{\Actions}{\mathcal{A}}
\newcommand{\action}{{\tt a}}
\newcommand{\States}{\mathcal{S}}
\newcommand{\state}{{\tt s}}
\newcommand{\transitionprob}{{\tt p}}
\newcommand{\ttime}{{\tt t}}
\newcommand{\tHorizon}{{\tt T}}
\newcommand{\weight}{{\tt w}}
\newcommand{\observation}{{\tt o}}
\newcommand{\thistory}{{\tt h}}
\newcommand{\Cost}{\mathcal{C}}
\newcommand{\cost}{{\tt c}}
\newcommand{\discount}{\gamma}
\newcommand{\Rmax}{{\tt R}_{\max }}
\newcommand{\Vmax}{{\tt V}_{\max }}
\newcommand{\reward}{{\tt r}}
\newcommand{\terminalreward}{r^T}
\newcommand{\histories}{\mathcal{H}}
\newcommand{\operator}{\mathcal{T}}
\newcommand{\policy}{\pi}
\newcommand{\Policies}{\Pi}

\newcommand{\reals}{\ensuremath{\mathbb{R}}}
\newcommand{\var}{\ensuremath{\mathrm{Var}}}
\newcommand{\E}{\ensuremath{\mathbb{E}}}
\renewcommand{\P}{\ensuremath{\mathbb{P}}}

