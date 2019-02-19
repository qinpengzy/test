{\rtf1\ansi\ansicpg936\cocoartf1561\cocoasubrtf600
{\fonttbl\f0\fnil\fcharset0 Monaco;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;\red83\green83\blue83;\red245\green245\blue245;\red40\green82\blue135;
\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c40000\c40000\c40000;\cssrgb\c96863\c96863\c96863;\cssrgb\c20000\c40000\c60000;
\cssrgb\c100000\c100000\c100000;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid1\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f0\fs24 \cf2 \cb3 {\listtext	1	}\expnd0\expndtw0\kerning0
import random\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	2	}\expnd0\expndtw0\kerning0
\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 {\listtext	3	}\expnd0\expndtw0\kerning0
print('------------------
\f1 \'ce\'d2\'b0\'ae\'d3\'e3
\f0 C
\f1 \'b9\'a4\'d7\'f7\'ca\'d2
\f0 ------------------')\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	4	}\expnd0\expndtw0\kerning0
secret = random.randint(1,10)\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \cb5 \kerning1\expnd0\expndtw0 {\listtext	5	}\expnd0\expndtw0\kerning0
temp = input("
\f1 \'b2\'bb\'b7\'c1\'b2\'c2\'d2\'bb\'cf\'c2\'d0\'a1\'bc\'d7\'d3\'e3\'cf\'d6\'d4\'da\'d0\'c4\'c0\'ef\'cf\'eb\'b5\'c4\'ca\'c7\'c4\'c4\'b8\'f6\'ca\'fd\'d7\'d6\'a3\'ba
\f0 ")\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 {\listtext	6	}\expnd0\expndtw0\kerning0
guess = int(temp)\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 {\listtext	7	}\expnd0\expndtw0\kerning0
\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \cb3 \kerning1\expnd0\expndtw0 {\listtext	8	}\expnd0\expndtw0\kerning0
while guess != secret:\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	9	}\expnd0\expndtw0\kerning0
\'a0 \'a0 temp = input("
\f1 \'b0\'a5\'d1\'bd\'a3\'ac\'b2\'c2\'b4\'ed\'c1\'cb\'a3\'ac\'c7\'eb\'d6\'d8\'d0\'c2\'ca\'e4\'c8\'eb\'b0\'c9\'a3\'ba
\f0 ")\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	10	}\expnd0\expndtw0\kerning0
\'a0 \'a0 guess = int(temp)\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	11	}\expnd0\expndtw0\kerning0
\'a0 \'a0 if guess == secret:\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	12	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0\'a0print("
\f1 \'ce\'d4\'b2\'db\'a3\'ac\'c4\'e3\'ca\'c7\'d0\'a1\'bc\'d7\'d3\'e3\'d0\'c4\'c0\'ef\'b5\'c4\'bb\'d7\'b3\'e6\'c2\'f0\'a3\'bf\'a3\'a1
\f0 ")\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	13	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0\'a0print("
\f1 \'ba\'df\'a3\'ac\'b2\'c2\'d6\'d0\'c1\'cb\'d2\'b2\'c3\'bb\'d3\'d0\'bd\'b1\'c0\'f8\'a3\'a1
\f0 ")\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	14	}\expnd0\expndtw0\kerning0
\'a0 \'a0 else:\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	15	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0\'a0if guess > secret:\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	16	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0 \'a0\'a0 \'a0print("
\f1 \'b4\'f3\'c1\'cb\'a3\'ac\'b4\'f3\'c1\'cb
\f0 ~~~")\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	17	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0\'a0else:\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	18	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0 \'a0\'a0 \'a0print("
\f1 \'d0\'a1\'c1\'cb\'a3\'ac\'d0\'a1\'c1\'cb
\f0 ~~~")\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	19	}\expnd0\expndtw0\kerning0
\'a0 \'a0\'a0 \'a0\'a0 \'a0\'a0 \'a0\cb1 \
\ls1\ilvl0\cb3 \kerning1\expnd0\expndtw0 {\listtext	20	}\expnd0\expndtw0\kerning0
print("
\f1 \'d3\'ce\'cf\'b7\'bd\'e1\'ca\'f8\'a3\'ac\'b2\'bb\'cd\'e6\'c0\'b2
\f0 ^_^")}