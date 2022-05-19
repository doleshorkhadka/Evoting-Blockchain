
# “eChunab”, an Online Voting System Using Blockchain

## Introduction
“eChunab” is an online web based voting system which allows specific audience or mass public to cast their vote safely and easily without breaking the daily routine. The web app can be used for specific institutions to choose their position and also used for nationwide elections for choosing the best leaders. As there are numerous disadvantages and bugs in the electronic voting system, our system is designed using a blockchain technology which is a secure and robust system that ensures anonymity of the voter, transparency in the process, robust Functioning and the decentralized system.The use of Ethereum on our web app enables the deployment of smart contracts and decentralized applications (dapps) to be built and ensure that the app will run without any interference from a third party. Also the transaction of the ethereum is fast which ensures the less time requirement for the voters to cast their vote and calculate the end result. The another purpose of using the transaction of ethereum is that it cannot be modified, hacked and controlled by intruder which makes the voting process transparent and legit. The electoral framework will have a node in every region to ensure that the system decentralized. This system can be used for a small scale organization. The blockchain technology and Face Detection is executed in web3.js and Python using the Flask framework respectively. The web page to caste vote is developed using HTML, CSS, and javascript along with the nodejs.User friendly web page ensure interactive site for casting votes and displaying outcomes and other essential information such as profile, candidate political background, the agenda of different political parties. The web page gives unquestionable visions for both nominees and voters. The two main module of our system are listed below:

- `Registration`: The sign-up feature along with face recognition for voters is set before the voting procedure starts. This features gathers the personal information which at last use for verification process.

- `Cast Vote`: Validate users/voters can cast a vote. The voter logins to cryptowallet and uses ethereum on a metamask to cast vote.

## Problem Statement
In the context of Nepal, Government uses traditional booth voting system which can be
easily modified and changed. The research of the traditional booth voting system leads us
to point out the following demerits: `Expensive`, `Insecure (as we heard booth capturing news)`, `Time consuming`, `Faults may rise in counting process`
So, to overcome the mentioned problem the government should goes for alternative way
i.e Electronic voting system. In centralized electronic voting system following problem
might arise:
    - `Data can be changed`
    - `Multiple entries can be registered`
    - `Manipulation of the result`
    - `Hacking of the entire system`
At last government should adapt the E-voting system which contains decentralized
database. For this purpose, our web app is suitable as it overcomes all the problems stated
below and has the following features:
    - `User friendly website with the ongoing elections list`
    - `Clock counting Deadline time`
    - `E-pamphlets of all political parties involved in elections`
    - `On screen result`
    - `Confidential Personal Info keeping and viewing at any time`

## Development Methodology
Development Methodology refers to structured processes involved when working on a
project. Its goal is to provide a systematic approach to develop a system. It also provides a
platform for developers to work together more efficiently as a team. It formalizes
communication and determines how information is shared within the team. Using a
software development methodology allows the team to cut down on inefficiency and
provide a more accurate delivery timeline. It prevents the team from reacting to every input,
but instead, allows them to be more organized and structured when dealing with
spontaneous changes.
Developers have high number of choices to select from various methodologies available.
Most of the methodologies falls under waterfall, iterative or continuous model. Among
these models, it was found that waterfall model is frequently used by different software
companies.
- Waterfall Development Model
It is a SDLC which is simple to understand and use. In waterfall model, each phase must
be completed before the next phase i.e. phases cannot overlap. In this approach, the
outcome of the one phases acts as an input for the next phase in a sequential way. Due to
this linear sequential flow, it is sometimes called as Linear-Sequential Life Cycle Model.
The following figure shows the different figure involved in waterfall model
<img src="/media/readmeimg/waterflow.png" alt="WATERFLOW MODEL"/>

## Use-Case Diagram
<img src="/media/readmeimg/usecase.png" alt="Use-case Diagram"/>

## Feasibility Analysis
Feasibility study is a high-level capsule version of the entire system analysis and design
process. The study begins by classifying the problem definition. The purpose of feasibility
study is to uncover the failing and robustness of an existing or proposed system. It is a
preliminary study conducted before the real development of the project ensuring project’s
success. A good research on feasibility study provides the historical background of the
project.
- Schedule Feasibility
It is the probability of a project to be completed within its scheduled time limits. The project
completed on-time has high schedule feasibility. The project will be unsuccessful if it takes 
13 longer timeframe than it was estimated. The following gantt chart shows eChunab is
accomplished on the given time interval which proves that it is feasible in terms of the
schedule.
<img src="/media/readmeimg/gantt.png" alt="Gantt Chart Diagram"/>

## Data Modelling using ER diagram
<img src="/media/readmeimg/er.png" alt="ER Diagram"/>

## Process Modelling using DFD diagram
<img src="/media/readmeimg/dfd.png" alt="DFD Diagram"/>

## System Design
**Database Design**
<img src="/media/readmeimg/design.png" alt="Database Design Diagram"/>

**Flow Chart**
<img src="/media/readmeimg/flowchart.png" alt="FlowChart Diagram"/>

## Implementation
**`Tools Used:`**
Programming Language is a high level language used to write a computer programs, which
allows programmers to write the source code in a natural fashion using logical words and
symbols. The major three programming language used are:
- Solidity: Solidity is an object-oriented, high-level language for implementing smart
contracts. Smart contracts are programs which governs the behavior of account with in
the Ethereum state. It is influenced by C++, Python, and Javascript and is designed to
target the Ethereum Virtual Machine(EVM). It is statically typed, supports inheritance,
libraries and complex user-defined types among other features. With solidity one can
create a crontracts for different uses such as voting, crowfunding, blind auctions, and
multi-signature wallets.
- Python: Python is an interpreted, object-oriented, high-level programming language
with dynamic semantics. Its high-level built in data structures, combined with dynamic
typing and dynamic binding, make it very attractive for RAD as well as for use as a
scripting components together. It’s simple, easy to learn syntax emphasizes readability
and therefore reduces the cost of program maintenance. It supports modules and
packages, which encourages program modularity and code reuse. The standard library
of python is free of cost and is available for all platforms.
- Java Script: JavaScript (js) is a light-weight object-oriented programming language
which is used by several websites for scripting the webpages. It is an interpreted, full-
fledged programming language that enables dynamic interactivity on websites when
applied to an HTML document. It was introduced in the year 1995 for adding programs
to the webpages in the Netscape Navigator browser. Since then, it has been adopted by
all other graphical web browsers. With JavaScript, users can build modern web
applications to interact directly without reloading the page every time. The traditional
website uses js to provide several forms of interactivity and simplicity. Although,
JavaScript has no connectivity with Java programming language. The name was
suggested and provided in the times when Java was gaining popularity in the market. In
addition to web browsers, databases such as CouchDB and MongoDB uses JavaScript
as their scripting and query language.For storing and retrieving the data, the most commonly used database i.e SQL is integrated.
SQLite databases are lightweight and easy to handle. In contrast to other database
frameworks, there is no setup, establishment needed to begin chipping away at an SQLite
Open database. We will kick off dealing with SQLite databases and tables
straightforwardly. SQLite provides the create database functionality to users, in which that
user can be able to create a database as per their requirement. SQLite gives you the
alternative of making another database (or opening a current one) each time you start the
order line utility. At the point when you use sqlite3 to begin the command line utility, you
can alternatively affix a data set document name.

**`Besides these other most important tools and technologies implemented in the system are:`**
- Truffle: A world class development environment, testing framework and asset pipeline
for blockchains using the Ethereum Virtual Machine (EVM), aiming to make life as a
developer easier.
- Etherium: Ethereum smart contracts are programs executed within the context of
transactions on the Ethereum blockchain. Ethereum Ganache forms part of the Truffle
Suite, a set of developer tools that allows users to recreate blockchain environments
locally and test smart contracts. Smart contract execution on the Ethereum blockchain is
very different from other types of software.
First of all, the on-chain context makes it hard to communicate with the outside world.
Simple input and output operations, such as writing to a console, are not possible, as
transactions are the only means of communicating with the blockchain. Secondly, the
transactional nature of the blockchain means that all state changing interactions with a
smart contract are asynchronous in nature. This means that when transactions are sent,
the effects are not visible until the transaction has been confirmed by being included in
a block. Finally, the blockchain environment places some specific restrictions on the
code that can be executed, mostly related to the cost associated with each operation.
Programmers have to consider factors such as the block gas limit, or how many
operations can be executed safely within the gas allowance of certain functions. In short,
smart contracts are hard to program. In addition, once deployed, smart contracts cannot
be modified and each deployment has an associated cost. Getting things right the first
time, therefore, has a criticality usually only associated with software in high-risk
applications such as control software in critical infrastructures or aviation. In order to
debug and test smart contracts before going into production, it is therefore essential to
21allow developers to recreate blockchain environments locally, without the added
inconvenience of deployment costs and transaction delays.Fortunately, the Truffle Suite,
a set of developer tools for Ethereum, includes Ethereum Ganache, a tool designed for
this purpose