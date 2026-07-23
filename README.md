# AI and MCP (Model Context Protocol) Workshop

```
Last updated 07/22/26
```

## **About Me**

### Link to recording of this workshop
- [View on PanOpto](https://nordvpn.com/link-checker/?srsltid=AfmBOopGtI-Joz1fRqE3V95zwog7rcU8HOFdvsICTwQM3tMMqkyYSTWo)
- [View on Youtube](https://nordvpn.com/link-checker/?srsltid=AfmBOopGtI-Joz1fRqE3V95zwog7rcU8HOFdvsICTwQM3tMMqkyYSTWo)


Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu
    


These workshops are offered by [research data services](https://data.library.virginia.edu/) in the UVA Libraries. Research Data Services does these things:
    
1. Find and Manage Data
2. Data Analysis & Visualization
3. Workshops & Trainings (Like this one!)
4. Free Statistics & Technical Consultations in the [StatLab](https://library.virginia.edu/data/statlab)

## StatLab
* [StatLab](https://library.virginia.edu/data/statlab)
The UVA Library StatLab provides free statistics & similar technical consulting to students, faculty, staff at UVA

## Upcoming Workshops

| Workshop | Date | Time |
| ---- | ---- | ---- |
| Change Me                                                |       Test 1/1   |  3:00 - 4:30pm
| Change Me                                                |       Test 1/1   |  3:00 - 4:30pm
| Change Me                                                |       Test 1/1   |  3:00 - 4:30pm
| Change Me                                                |       Test 1/1   |  3:00 - 4:30pm
| Change Me                                                |       Test 1/1   |  3:00 - 4:30pm


----------------------------------------------------------------------------------------------------
In the AI-enabled world that we live in, a new technology is becoming more prevalent, **MCP (Model Context Protocol)**.

## Precursor - What is an API?
Personally, I like to think of MCP as an evolution to pre-existing systems, such as APIs. So let's cover a little background first. 

*The following excerpt is taken from [this site](https://www.mulesoft.com/resources/api/what-is-an-api)*
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. By establishing a common set of rules for exchanging information, APIs make it easier for two parties to communicate with eachother. Each time you use an app like Instagram, find a song you like on Spotify, or check the weather on your phone, you’re using an API.

For example, when you use an application on your device, the application connects to the Internet and sends data to a server. The server then receives that data, interprets it, performs the response which might involve sending data back to you. The API states the rules in order for this communication to happen. 

An analog example in real life...
If you go to a restaurant, you sit down at a table and look at a menu. The server comes and takes your order. Your order is then taken to the kitchen where they prepare the food. In this case, the server is the API, which is a layer of interaction between the client and the kitchen. You (probably) can't go directly into the kitchen and order food. The waiter is the intermediary that takes your information and interprets it into a form the kitchen can understand. The response (the food in this case) is then sent back to you, the client. 

A common API architectural style is **REST**, which relies on the HTTP protocol and **JSON** data format to send and receive messages. It is a set of rules that developers follow when they create their API. One of these rules states that you can get a piece of data (called a resource) when you send a request to a specific URL. 

Good example of a REST API: [https://newsapi.org/](https://newsapi.org/)


## What is MCP?
MCP, or Model Context Protocol, is an open-source standard created by Anthropic that gives a universal way for AI applications to connect to local files, databases, external applications, etc. MCP bridges AI and your data in a three part system.

- Host. This is the main AI application you are using (ex: Claude Desktop)
- Client. The component in the application that manages your connection to outside resources
- Server. A lightweight program that securely talks to your data and translates it into a format the AI understands. 
