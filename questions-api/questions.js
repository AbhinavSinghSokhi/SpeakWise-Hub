const { UserInputError } = require("apollo-server-express");
const res = require("express/lib/response");
const { getDb, getNextSequence } = require("./db.js");
const OpenAI = require("openai");

async function get(_, { article }) {
  //   const db = getDb();
  const openai = new OpenAI({
    apiKey: process.env.OPEN_API_KEY,
  });
  const chatCompletion = await openai.chat.completions.create({
    messages: [
      {
        role: "user",
        content: `formulate a single question from this paragraph. The output format must be as: Question: <question> Answer: <answer>. The article is: ${article.content}`,
      },
    ],
    model: "gpt-3.5-turbo",
  });
  console.log(
    chatCompletion.choices[0].message.content
      .split("Question: ")[1]
      .split("Answer: ")[0]
  );
  question = chatCompletion.choices[0].message.content
    .split("Question: ")[1]
    .split("Answer: ")[0];
  answer = chatCompletion.choices[0].message.content
    .split("Question: ")[1]
    .split("Answer: ")[1];
  return { question, answer };
}

module.exports = { get };
