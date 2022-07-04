/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.munene.converter;

/**
 *
 * @author munene
 */
import java.net.*;
import java.io.*;
import java.util.*; 
public class Server {
    	public static void main (String[] args) throws IOException {
	ServerSocket ss = new ServerSocket(4999);
	Socket s = ss.accept();

	System.out.println("Client connected ");

	InputStreamReader in = new InputStreamReader(s.getInputStream());
	BufferedReader bf = new BufferedReader(in);

	String str = bf.readLine();
	System.out.println("Client: "+ str);

	PrintWriter pr = new PrintWriter(s.getOutputStream());
		
		pr.println(str.toUpperCase());
		pr.flush();

	}
}
