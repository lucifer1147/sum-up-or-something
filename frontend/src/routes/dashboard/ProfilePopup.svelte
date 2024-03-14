<script>
	import { pos, visible } from './store.js';
	
	export let height;

	const handleKeyDown = (e, type) => {
		let trueCondition = true;
		if (type === 'key') {
			trueCondition = e.keyCode === 17;
		}

		if (trueCondition) {
			if ($pos !== 'left-0') {
				pos.set('left-0');
				visible.set('opacity-100 z-[10]');
			} else {
				pos.set('left-[-25%]');
				visible.set('opacity-0 z-[-10]');
				handleMouseEvent(e, 'close')
			}
		}
	};
</script>

<div
	class={height +
		' w-full bg-gray-700 my-2 rounded-lg text-white overflow-hidden box-border flex items-center flex-wrap'}
>
	<ul class="p-4 font-semibold font-mono w-full">
		<li class="h-7 w-full hover:bg-gray-600 flex items-center text-lg rounded-md">
			<a href="/user/profile" class="px-2 py-2 h-full w-full flex items-center">Profile</a>
		</li>
		<li class="h-7 w-full hover:bg-gray-600 flex items-center text-lg rounded-md">
			<a href="/user/settings" class="px-2 h-full w-full flex items-center">Settings</a>
		</li>
		<hr class="my-2" />
		<li class="h-7 w-full hover:bg-gray-600 flex items-center text-lg rounded-md">
			<a href="/about/contact-us" class="px-2 h-full w-full">Contact Us</a>
		</li>
		<li class="h-7 w-full hover:bg-gray-600 flex items-center text-lg rounded-md">
			<a href="/about" class="px-2 h-full w-full">About Us</a>
		</li>
		<hr class="my-2" />
		<li class="h-7 w-full hover:bg-gray-600 flex items-center text-lg rounded-md">
			<a href="/logout" class="px-2 h-full w-full">Logout</a>
		</li>
	</ul>
</div>
