package WebScrapper;

import java.io.IOException;
import java.io.PrintWriter;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;


public class WebScraper 
{
	
	public static void main (String[]  args)
	{
		Document doc;
		int count = 0;
		PrintWriter writer;
		String city = "key+biscayne";
		try 
		{
			writer = new PrintWriter( ("data" + city + ".txt"), "UTF-8");
			
		
	
			for(int j = 1 ; j < 101 ; j++){
				try 
				{
					doc = Jsoup.connect("http://mugshots.com/search.html?q="+ city + "&page=" + j).get();//Create a http connection to url, get the DOM, and store it into Document doc
					Elements info = doc.select("img");//Select all the 'a' elements in the document and store it into the Elements variable info
					 //info = info.select("img");
					for (Element i : info)//for each Element i in info
					{
						
						//System.out.println(i.attr("href"));//print out the attribute of href
		
							//if(i.attr("width").equals("195"))
								if(!i.attr("src").contains("logo") && !i.attr("src").contains("mobile")){
									System.out.println( count + ": <img src=\"" + i.attr("src") + "\"></img>" );//+ "\nWIDTH:" + i.attr("width"));
									writer.println(i.attr("src"));
									count++;
								}
					}
				} 
				catch (IOException e) 
				{
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
			System.out.println("COUNT: " + count);
			writer.println("COUNT: " + count);
			writer.close();
		}
		catch(Exception e){
			
		}
		
		
	}

}
