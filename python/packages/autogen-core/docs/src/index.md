---
myst:
  html_meta:
    "description lang=en": |
      Top-level documentation for AutoGen, a framework for developing applications using AI agents
html_theme.sidebar_secondary.remove: false
sd_hide_title: true
---

<style>
.hero-title {
  font-size: 45px !important;
  font-weight: bold;
  margin: 2rem auto 0 !important;
}
button.gs-button {
  margin: 4px 0px 5px 0px;
  padding: 6px 12px 6px 12px;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  font-size: 15px;
}
.version-text{
  font-size: 12px;
  color: #6c757d;
  font-weight: normal;
}   
.logo {
  width: 50px;
  height: 50px; 
  margin-bottom: 30px;
  display: inline-block;
}
</style>

# AutoGen

<div class="container">
   
<div class="row text-center">
<div class="col-sm-12">
<!-- <span class="version-text">v0.4.0-dev released </span> -->
<h1 class="hero-title">
<img src="_static/images/logo/logo.svg" alt="AutoGen" class="logo" />
AutoGen 
</h1>
<h3>
A framework for developing applications using AI agents
</h3>
</div>
</div>

::::{grid} 2
:::{grid-item-card} {fas}`people-group;pst-color-primary` AgentChat
For Beginners
^^^
A High-level API include preset agents and teams for building multi-agent systems.

+++

<button onclick="location.href='agentchat-user-guide/quickstart.html'" class="gs-button col-sm">Get Started</button>

:::
:::{grid-item-card} {fas}`cube;pst-color-primary` Core
For Advanced Users
^^^
Provides building blocks for creating asynchronous, event driven multi-agent systems.

+++
<button onclick="location.href='core-user-guide/guides/quickstart.html'" class="gs-button col-sm">Get Started</button>
:::
::::

<br/>
<br/>

::::{grid} 2

:::{grid-item}

## Gettting Started

<br />
AgentChat makes it easy to create apps where multiple agents interact to solve tasks.

<br />
<br />

<button onclick="location.href='agentchat-user-guide/examples/index.html'" class="gs-button col-sm">View Examples &nbsp; {fas}`angle-right;pst-color-primary`</button>

:::
:::{grid-item}
![AgentChat](./images/code.svg)
:::

::::

```{versionadded} 0.4x
The sample code below show a simple example of generating a stock price visualization in  using **AgentChat** (0.4) and 0.2 versions of AutoGen.
```

```{include} agentchat-user-guide/stocksnippet.md

```

```{toctree}
:maxdepth: 3
:hidden:

agentchat-user-guide/index
```

```{toctree}
:maxdepth: 3
:hidden:

core-user-guide/index
```

```{toctree}
:maxdepth: 1
:hidden:
packages/index
```

```{toctree}
:maxdepth: 1
:hidden:
reference/index
```
