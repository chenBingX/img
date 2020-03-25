# 趁手利器，FSuper

现在，我需要向你隆重介绍，即将在你的 **Flutter** 编程之路中，令你爱不释手的 **趁手利器** —— **FSuper**。

**FSuper** 是 **[【阿里巴巴飞猪 Fliggy Android Team
 技术团队】](https://github.com/Fliggy-Android-Team)** 开发的 **FWidgets** 系列组件之一。是由 **[Github 2.8k+ star 项目 《SuperTextView》](https://github.com/chenBingX/SuperTextView)** 作者 **CoorChice** 操刀制作开发的 **Flutter** 组件。

 它能够助你十分便捷的实现诸多视觉效果。

 它所支持的布局方式能够轻松拆解构建绝大部分复杂布局。

 它让好，更好一点！


## 特性

来看看 **FSuper** 能为你带来些什么？

- 丰富的**边角**效果

- 精美的**边框**装饰

- 天然支持精彩的**富文本**

- **渐变效果**也不在话下

- 更具空间感的**阴影**

- 不简单的**小红点**

- 灵活且强大的**相对位置布局**


# 边角

> ***随心所欲，彰显个性。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_边角.jpg)

**FSuper** 支持灵活、丰富的边角设置。圆角、斜角、1个、2个、..，你大可随心所欲。

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_边角code.jpg)

仅需两个属性 `corner`、`cornerStyle`，就能构建千奇百怪的边角效果。


# 边框

> ***简单一点，再简单一点。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_边框.jpg)

为 **FSuper** 添加边框，足够简单。

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_边框code.jpg)

只需 `strokeColor` 和 `strokeWidth` 属性搭配，即可立即获得令人满意的边框装饰效果。即使是再加上边角效果，同样也足够简单。


# 富文本

> ***浑然天成，一步到位。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_富文本.jpg)

**FSuper** 天然支持了直接配置富文本效果，而无需开发者增加而外的组件。一切都在 **FSuper** 中完成。

```
FSuper(
  // #1
  text: "En.. ",
  spans: [
    // #2
    TextSpan(
        text: "FWidget",
        style: TextStyle(
          color: Color(0xffffc900),
          backgroundColor: Colors.black38,
          fontSize: 20,
        )),
    // #3
    TextSpan(text: " are really "),
    // #4
    TextSpan(
        text: "delicious",
        style: TextStyle(
          color: Colors.blue,
          fontSize: 20,
          fontStyle: FontStyle.italic,
        )),
    // #5
    TextSpan(text: "!"),
    // #6
    TextSpan(
      text: "\nYou can try to ",
    ),
    // #7
    TextSpan(
      text: "click here",
      style: TextStyle(
        color: Colors.redAccent,
        fontSize: 18,
        decoration: TextDecoration.underline,
        decorationColor: Colors.blue,
        decorationStyle: TextDecorationStyle.wavy,
      ),
      recognizer: TapGestureRecognizer()
        ..onTap = () {
          _showDialog(
              context, "YA! How dare you clicked me?");
        },
    ),
    // #8
    TextSpan(text: " !"),
  ],
),
```

**FSuper** 将 **Flutter** 所提供的富文本支持进行了精巧的融合，使得在兼具 **FSuper** 所提供的一切能力的前提下，不用引入新的组件，而能够支持富文本。这真是太棒了👏！



# 渐变效果

> ***色彩够多，才够出彩。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_渐变.jpg)

通过 `gradient` 属性，你可以直接为 **FSuper** 直接配置 **LinearGradient**、**RadialGradient**、**SweepGradient** 等多种渐变色背景效果。

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_渐变code.jpg)

**FSuper** 在削减层级嵌套上，始终是一把利器。


# 阴影

> ***要多立体，都行！***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_阴影.jpg)

**FSuper** 通过简单的 `shadowColor` 和 `shadowBlur` 属性即可控制组件阴影的颜色、大小。

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_阴影code.jpg)

代码虽然的简单，但是立体效果绝对不简单。



# 小红点

> ***内藏玄机，妙不可言。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_小红点.jpg)

**FSuper** 为你铺平了构建小红点效果的坎坷道路。关于小红点位置确定的相关计算，由 **FSuper** 完成。你只需要关注你需要什么就够了。

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_小红点code.jpg)

这是显而易见的改变，从此构建小红点不在话下。

# 相对位置布局

> ***再复杂，也简单。***

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_布局1.jpg)

![](https://raw.githubusercontent.com/chenBingX/img/master/Flutter/fsuper/fsuper_布局2.jpg)


