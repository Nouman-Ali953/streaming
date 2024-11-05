<template>
    <div>
      <h1>Data Stream</h1>
      <p class="paragraph" v-html="formattedChunks"></p>
    </div>
  </template>
  
  <script>
  export default {
    name: "DataStream",
    data() {
      return {
        chunks: []  // Array to store each word/phrase streamed from backend
      };
    },
    computed: {
      formattedChunks() {
        // Join the chunks with a space and return as HTML
        return this.chunks.join(' '); // Join chunks with a space
      }
    },
    mounted() {
      this.startStreaming();
    },
    methods: {
      startStreaming() {
        const eventSource = new EventSource("http://127.0.0.1:5000/api/stream");
        
        eventSource.onmessage = (event) => {
          this.chunks.push(event.data);  // Append each word or chunk to the chunks array
        };
  
        eventSource.onerror = () => {
          eventSource.close();  // Close stream on error
        };
      }
    }
  };
  </script>
  
  <style scoped>
  .paragraph {
    width: 98%;
    display: block;
    padding: 10px;
    border-radius: 4px;
    font-size: 16px;
    line-height: 1.5;
  }
  h1 {
    color: #333;
    font-weight: bold;
  }
  </style>
  