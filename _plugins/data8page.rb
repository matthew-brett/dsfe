=begin

This Jekyll plugin installs a new Liquid tag to note that our page has text from the UCB data8 original.

Use with:

{% data8page page_name %}

where "page_name" is the name of the page in the data8 site.

=end
require "jekyll"

class Data8Page < Liquid::Tag

    def initialize(tagname, markup, tokens)
        @markup = markup.strip
        super
    end

    def render(context)
        if @markup.empty?
            return "Error processing input, expected syntax: {% data8page name %}"
        end

        # Render the markup
        parameters = Liquid::Template.parse(@markup).render context
        parameters.strip!

        <<EOT
<div markdown="1" class="note">
This page has content from the `#{parameters}` page of the UC Berkeley course.
See the Berkeley course section of the [license]({{ site.baseurl }}/license)
</div>
EOT
    end

    Liquid::Template.register_tag("data8page", self)
end
