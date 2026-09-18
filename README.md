# AI and MCP (Model Context Protocol) Workshop

```
Last updated 09/18/26
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
| Intro to Python pt 1                                                |       Tuesday 9/1   |  11:00am - 12:30pm
| Intro to Python pt 2                                                |       Friday  9/4   |  11:00am - 12:30pm
| Local Large (and small) Language Models                             |       Tuesday 9/8   |  11:00am - 12:30pm
| Vibe Coding & AI Agents                                             |       Tuesday 9/15  |  11:00am - 12:30pm
| AI and Model Context Protocol                                       |       Tuesday 9/22  |  11:00am - 12:30pm
| Ethical AI Use & Best Practices                                     |       Tuesday 9/29  |  11:00am - 12:30pm


----------------------------------------------------------------------------------------------------
In the AI-enabled world that we live in, a new technology is becoming more prevalent, **MCP (Model Context Protocol)**.

## What is MCP?
MCP, or Model Context Protocol, is an open-source standard created by Anthropic that gives a universal way for AI applications to connect to outside tools and data sources. Before MCP, every AI application had to build a custom one-off integration for each tool it wanted to use. If you think about an AI tool you use, how many integrations might it have? A lot! This exponentially increased the amount of work for people to make their tools usable. 

## History Lesson - Precursor to MCP, including protocols/standards
I will start with **standards** and **protocols**. A standard is an official, agreed-upon rulebook or set of specifications, while a protocol is the specific step-by-step procedure or language used to carry out an action within those rules. Most pieces of tech, whether it be a physical device like a USB-C drive, or internet protocol like HTTP, follows a standard. This allows different systems around the world to be interoperable. 

Before the MCP protocol, AI models relied on functions to call, which were written by developers. This had to be done separately fo revery application that wants to use that function. For example, if you build a weather-lookup function for one chatbot, you couldn't just hand it to a different AI application. The team would have had to re-write another function. Basically the foundation of the MCP framework are APIs. There was no AI involved in deciding how or when to call an API, this was all written by a human. 

##### What is an API?
Personally, I like to think of MCP as an evolution to pre-existing systems, such as APIs. So let's cover a little background first. 

*The following excerpt is taken from [this site](https://www.mulesoft.com/resources/api/what-is-an-api)*
API is the acronym for Application Programming Interface, which is a software intermediary that allows two applications to talk to each other. By establishing a common set of rules for exchanging information, APIs make it easier for two parties to communicate with eachother. Each time you use an app like Instagram, find a song you like on Spotify, or check the weather on your phone, you’re using an API.

For example, when you use an application on your device, the application connects to the Internet and sends data to a server. The server then receives that data, interprets it, performs the response which might involve sending data back to you. The API states the rules in order for this communication to happen. 

An analog example in real life...
If you go to a restaurant, you sit down at a table and look at a menu. The server comes and takes your order. Your order is then taken to the kitchen where they prepare the food. In this case, the server is the API, which is a layer of interaction between the client and the kitchen. You (probably) can't go directly into the kitchen and order food. The waiter is the intermediary that takes your information and interprets it into a form the kitchen can understand. The response (the food in this case) is then sent back to you, the client. 

A common API architectural style is **REST**, which relies on the **HTTP protocol** and **JSON** data format to send and receive messages. It is a set of rules that developers follow when they create their API. One of these rules states that you can get a piece of data (called a resource) when you send a request to a specific URL. 

Good example of a REST API: [https://newsapi.org/](https://newsapi.org/)


## TLDR: How is MCP different from an API?
The key difference between MCPs and APIs is their intended user. In the past, APIs required a human to call them. Now, MCP allows LLMs to use APIs with some other information attached. Now, MCP is like a USB-C port. You can plug many things into a USB-C port because it is a universal standard outlet. 


## Core Concepts of MCP
Client/server model: the AI app is the client. The tool and data are the server.
There are three things a server can expose:
- Tools (actions the AI can invoke)
- Resources (data/context the AI can read)
- Prompts (reusable templates)

To say a little more, the client is the AI LLM which makes requests. Often times that is via a human user. If you are using a chatbot like Claude, ChatGPT, Gemini, you are making requests to the client. The server runs in the background, waiting for requests from the client and it fulfills those with a response of some kind. 

The first step in this process is the client asks the server: "What can you do?". The server responds with a structured list of all it's capabilities which are tools, resources, and prompts. This is why MCP is usable across all compatible applications. Nothing is hard-coded on the client side about what a specific server does. It is all discovered dynamically when a connection is made. AI doesn't automatically use everything a server exposes. Tols are invoked selectively based on the conversation. 


## Code Example 1: Minimal MCP server. Connect client and call it with AI
In this minimalist code example, I'm going to walk through a simple setup for an MCP client and server. This is using the recommended basic setup from the [MCP Python SDK documentation](https://py.sdk.modelcontextprotocol.io/). For the client file, I am using a LLM that I installed locally on my own computer (llama3.2 in this case). [Installing local LLMs is another side-topic which I have taught an entire workshop on](https://github.com/epurpur/Local_LLM_Workshop). 

In our walkthrough, we have
- only 2 files, server.py and client.py
- Bare bones server.py setup. The server provides tools, resources, and prompts
- 

## Real World use cases
**Slack** - Slack is a messaging platform commonly used in business. The UVA Library organization uses it for internal communication. The Slack MCP server lets AI search channels, read conversation context, and act inside the workspace. The "agents and apps" is a great example of MCP integration. These are other services that Slack can embed and interact with.  











