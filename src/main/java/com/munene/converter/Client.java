/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.munene.converter;

/**
 *
 * @author munene
 */
import java.net.*;
import java.io.*;
import java.util.*; 

public class Client{
	public static void main (String[] args) throws IOException {
	Socket s = new Socket("localhost",4999);

	PrintWriter pr = new PrintWriter(s.getOutputStream());

	Scanner sc= new Scanner(System.in);    //System.in is a standard input stream  
	System.out.print("Enter message: ");  
	String stri= sc.nextLine();      
	pr.println(stri);
	pr.flush();

	InputStreamReader in = new InputStreamReader(s.getInputStream());
	BufferedReader bf = new BufferedReader(in);

	String str = bf.readLine();
	System.out.println("Server: "+ str);

}

}