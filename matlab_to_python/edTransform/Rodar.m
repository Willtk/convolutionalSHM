close all
clear all
clc
disp('ploting')

%Rotina (tran) para conversao dos dados com separação de "virgula" POR "PONTO". O
%sistema de aquisição do Labview está "," e o matlab trabalha com "ponto".
%Assim, essa função so faz isso. Ela procura as , troca as por pontos e
%salva em cima.

 tran('Imp_d1_1_1Sensor1_1.lvm')
  tran('Imp_d1_1_1Sensor1_2.lvm')
  tran('Imp_d1_1_1Sensor1_3.lvm')
  tran('Imp_d1_1_1Sensor1_4.lvm')
 tran('Imp_d1_1_1Sensor1_5.lvm')
 tran('Imp_d1_1_1Sensor1_6.lvm')
 tran('Imp_d1_1_1Sensor1_7.lvm')
 tran('Imp_d1_1_1Sensor1_8.lvm')
  tran('Imp_d1_1_1Sensor1_9.lvm')
  tran('Imp_d1_1_1Sensor1_10.lvm')
  tran('Imp_b_1Sensor1_3.lvm')

%%%%%%%%%%%%%%%%%%%%%%%%%%%
%Entrada de dados. os sinais com danos foram coletados no PZT1 por 30
%vezes repetidas.
%%%%%%%%%%%%%%%%%%%%%%%%%%

a1= load('Imp_d1_1_1Sensor1_1.lvm');%(com dano)
a2=a1(:,3); %seleciona a parte real da impedância
a=a2(10000:39999); %limita os sinais

b1=load ('Imp_d1_1_1Sensor1_2.lvm');%(com dano)
b2=b1(:,3);
b=b2(10000:39999);

c1=load('Imp_d1_1_1Sensor1_3.lvm');%(com dano)
c2=c1(:,3);
c=c2(10000:39999);

d1=load('Imp_d1_1_1Sensor1_4.lvm');%(com dano)
d2=d1(:,3);
d=d2(10000:39999);

e1=load('Imp_d1_1_1Sensor1_5.lvm');%(com dano)
e2=e1(:,3);
e=e2(10000:39999);

f1=load('Imp_d1_1_1Sensor1_6.lvm');%(com dano)
f2=f1(:,3);
f=f2(10000:39999);

g1=load('Imp_d1_1_1Sensor1_7.lvm');%(com dano)
g2=g1(:,3);
g=g2(10000:39999);

h1=load('Imp_d1_1_1Sensor1_8.lvm');%(com dano)
h2=h1(:,3);
h=h2(10000:39999);

i1=load('Imp_d1_1_1Sensor1_9.lvm');%(com dano)
i2=i1(:,3);
i=i2(10000:39999);

j1=load('Imp_d1_1_1Sensor1_10.lvm');%(com dano)
j2=j1(:,3);
j=j2(10000:39999);

l1=load('Imp_b_1Sensor1_3.lvm'); %baseline (sem dano)
l2=l1(:,3);
l=l2(10000:39999);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
 %a função abaixo, nesse caso específico quebra o sinal em 10 partes de
 %3000 amostras cada
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
lMa=reshape(l, 3000, 10);
aMa = reshape(a, 3000, 10); %// For plot3
bMa = reshape(b, 3000, 10); %//For plot3
cMa = reshape(c, 3000, 10); %//For plot3
dMa = reshape(d, 3000, 10); %// For plot3
eMa = reshape(e, 3000, 10); %//For plot3
fMa = reshape(f, 3000, 10); %//For plot3
gMa = reshape(g, 3000, 10); %// For plot3
hMa = reshape(h, 3000, 10); %//For plot3
iMa = reshape(i, 3000, 10); %//For plot3
jMa = reshape(j, 3000, 10); %// For plot3

aMat=[lMa aMa];  % junta num vetor os "valores quebrados" do baseline (lMa) com outra condição qualquer. Nestes casos com danosa (aMa).
bMat=[lMa bMa];
cMat=[lMa cMa];
dMat=[lMa dMa];
eMat=[lMa eMa];
fMat=[lMa fMa];
gMat=[lMa gMa];
hMat=[lMa hMa];
iMat=[lMa iMa];
jMat=[lMa jMa];

%_________________________________________
%Calcula a distância Euclideana entre os vetores acima.
%________________________________________

A_1 = pdist(aMat','minkowski'); % Calcula a distancia euclidiana utilizando Minkowski
Z_1 = squareform(A_1); % coloca valores na forma matriz quadrada
H1 = Z_1 ./ max(Z_1(:)); % Normalização dos valores em relação ao valor máximo

A_2 = pdist(bMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_2 = squareform(A_2); %coloca valores na forma matriz quadrada
H2 = Z_2 ./ max(Z_2(:)); %Normalização dos valores em relação ao valor máximo

A_3 = pdist(cMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_3 = squareform(A_3); %coloca valores na forma matriz quadrada
H3 = Z_3 ./ max(Z_3(:)); %Normalização dos valores em relação ao valor máximo

A_4 = pdist(dMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_4 = squareform(A_4); %coloca valores na forma matriz quadrada
H4 = Z_4 ./ max(Z_4(:)); %Normalização dos valores em relação ao valor máximo

A_5 = pdist(eMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_5 = squareform(A_5); %coloca valores na forma matriz quadrada
H5 = Z_5 ./ max(Z_5(:)); %Normalização dos valores em relação ao valor máximo

A_6 = pdist(fMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_6 = squareform(A_6); %coloca valores na forma matriz quadrada
H6 = Z_6 ./ max(Z_6(:));%Normalização dos valores em relação ao valor máximo

A_7 = pdist(gMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_7 = squareform(A_7); %coloca valores na forma matriz quadrada
H7 = Z_7 ./ max(Z_7(:)); %Normalização dos valores em relação ao valor máximo

A_8 = pdist(hMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_8 = squareform(A_8); %coloca valores na forma matriz quadrada
H8 = Z_8 ./ max(Z_8(:)); %Normalização dos valores em relação ao valor máximo

A_9 = pdist(iMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_9 = squareform(A_9); %coloca valores na forma matriz quadrada
H9 = Z_9 ./ max(Z_9(:)); %Normalização dos valores em relação ao valor máximo

A_10 = pdist(jMat','minkowski'); %Calcula a distancia euclidiana utilizando Minkowski
Z_10 = squareform(A_10); %coloca valores na forma matriz quadrada
H10 = Z_10 ./ max(Z_10(:)); %Normalização dos valores em relação ao valor máximo

%######################################################
%PLOTA OS FRAMES NO FORMATO rgb e os salva no diretorio
%####################################################
figure
image(H1,'CDataMapping','scaled')
colormap
saveas(gcf,'d1.jpg') %SALVAS OS FRAMES NO DIRETÓRIO

figure
image(H2,'CDataMapping','scaled')
colormap
saveas(gcf,'d2.jpg')

figure
image(H3,'CDataMapping','scaled')
colormap
saveas(gcf,'d3.jpg')

figure
image(H4,'CDataMapping','scaled')
colormap
saveas(gcf,'d4.jpg')

figure
image(H5,'CDataMapping','scaled')
colormap
saveas(gcf,'d5.jpg')

figure
image(H6,'CDataMapping','scaled')
colormap
saveas(gcf,'d6.jpg')

figure
image(H7,'CDataMapping','scaled')
colormap
saveas(gcf,'d7.jpg')

figure
image(H8,'CDataMapping','scaled')
colormap
saveas(gcf,'d8.jpg')

figure
image(H9,'CDataMapping','scaled')
colormap
saveas(gcf,'d9.jpg')

figure
image(H10,'CDataMapping','scaled')
colormap
saveas(gcf,'d10.jpg')

 disp('done') 
