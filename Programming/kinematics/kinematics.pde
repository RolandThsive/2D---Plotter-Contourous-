
float q1;
float q2;

float x0= 500;
float x1;
float endX;

float y0 =500;
float y1;
float endY;

float a1 =221.86;
float a2 =121.86;

float reach = a1+a2;

void setup(){
 size(1000,1000); 
}

void draw() {
  strokeWeight(20);
  background(0);
  
  
  //line(500,500,500,500+reach);
  
  endX=int(mouseX);
  endY=int(mouseY);
  
  float triedDist = sqrt( pow(x0-endX,2) + pow(y0-endY,2) );
  

  if(reach > triedDist){
    stroke(0,0,255);
    circle(500,500,reach*2);
    
    q2 = acos( (pow(endX-x0,2)+pow(endY-y0,2)-pow(a1,2)-pow(a2,2)) / (2*a1*a2) );
    q1=atan2( (endY-y0) , (endX-x0)) + atan2( (a2*sin(q2)) , (a1+a2*cos(q2)) );

    println("q1: "+q1+"   q2: "+q2);
    
    x1= int(x0+ a1*cos(q1));
    y1= int(y0+a1*sin(q1));

     
    float printA1 = sqrt( pow(x1-x0,2) + pow(y1-x0,2));
    float printA2 = sqrt ( pow(endX-x1,2) + pow(endY-y1,2));
    println("-----------");
    println("a1: "+printA1+"   a2: "+printA2);
    println("q1: "+q1+"   q2: "+q2);
  
    stroke(0,0,255);
    line(x0,y0,x1,y1);
    stroke(0,255,0);
    line(x1,y1,endX,endY);
    stroke(255,0,0);
    circle(endX,endY,50);
    stroke(0);
    line(endX-50,endY-50,endX+50,endY+50);
  } else {
    stroke(255,0,0);
    circle(500,500,reach*2);
    stroke(255,0,0);
    line(x0,y0,endX,endY);
  }
}
